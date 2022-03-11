import socketserver
import sys
import json
from .logger import getLogger
from .cache import Cache


class CacheRequestHandler(socketserver.BaseRequestHandler):
    _MAX_LENGTH = 1024
    _CACHE = Cache()

    def __init__(self, request, client_address, server):
        self.logger = getLogger('CacheRequestHandler')
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)

    def setup(self):
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):
        dataReceived = b''
        while True:
            data = self.request.recv(CacheRequestHandler._MAX_LENGTH)
            if not data:
                break
            dataReceived += data
            if len(str(data)) < CacheRequestHandler._MAX_LENGTH:
                break
        response = self.process(dataReceived)
        response = bytes(json.dumps(response), "utf-8")
        self.request.sendall(response)

    def process(self, dataReceived):
        response = {
            "status": "SUCCESS",
        }
        try:
            jsonAsString = str(dataReceived, 'utf-8')
            jsonAsObject = json.loads(jsonAsString)
            operation = jsonAsObject["operation"]
            data = jsonAsObject["data"]
            name = None
            timeAlive = None
            outputCache = {}
            if "tableName" in data and data["tableName"]:
                name = data["tableName"]
            if "timeAlive" in data and data["timeAlive"]:
                timeAlive = data["timeAlive"]
            if operation == "GET":
                if "key" not in data:
                    raise Exception("key not found")
                key = data["key"]
                outputCache = CacheRequestHandler._CACHE.get(key, name)
            if operation == "GET_ALL":
                outputCache = CacheRequestHandler._CACHE.getAll(name)
            elif operation == "SET":
                if "key" not in data:
                    raise Exception("key not found")
                if "value" not in data:
                    raise Exception("value not found")
                key = data["key"]
                value = data["value"]
                outputCache = CacheRequestHandler._CACHE.set(key, value, timeAlive, name)
            elif operation == "REMOVE":
                if "key" not in data:
                    raise Exception("key not found")
                key = data["key"]
                outputCache = CacheRequestHandler._CACHE.remove(key, name)
            elif operation == "SIZE":
                outputCache = CacheRequestHandler._CACHE.size(name)
            elif operation == "CLEAN":
                outputCache = CacheRequestHandler._CACHE.clean(name)
            response = {**response, **outputCache}
        except Exception as e:
            print(e)
            response["status"] = "ERROR"
            response["error"] = str(e)
        return response

    def finish(self):
        self.logger.debug('finish')
        return socketserver.BaseRequestHandler.finish(self)

if __name__ == '__main__':
    try:
        pass
    except KeyboardInterrupt as e:
        sys.exit(0)
