import socket
import json


class CacheAxClient(object):
    _MAX_LENGTH = 1024

    def __init__(self, port=63456, ip="0.0.0.0", options=None):
        self.ip = ip
        self.port = port
        self.options = options
        self.client = None

    def stringToJson(self, st):
        try:
            return json.loads(st)
        except:
            pass
        return st

    def __close(self):
        if self.client:
            self.client.close()

    def __open(self):
        self.__close()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip, self.port))

    def __receiveMessage(self):
        dataReceived = b''
        while True:
            data = self.client.recv(CacheAxClient._MAX_LENGTH)
            if not data:
                break
            dataReceived += data
            if len(str(data)) < CacheAxClient._MAX_LENGTH:
                break
        response = str(dataReceived, "utf-8")
        return self.stringToJson(response)

    def __sendMessage(self, message):
        try:
            self.__open()
            dataAsString = json.dumps(message)
            self.client.send(dataAsString.encode())
            return self.__receiveMessage()
        except:
            pass
        finally:
            self.__close()

    def get(self, key, name=""):
        request = {
            "operation": "GET",
            "data": {
                "tableName": name,
                "key": key,
            }
        }
        return self.__sendMessage(request)

    def getAll(self, name=""):
        request = {
            "operation": "GET_ALL",
            "data": {
                "tableName": name
            }
        }
        return self.__sendMessage(request)

    def set(self, key, value, name=""):
        timeAlive = None
        if self.options and "timeAlive" in self.options and self.options["timeAlive"]:
            timeAlive = self.options["timeAlive"]
        request = {
            "operation": "SET",
            "data": {
                "tableName": name,
                "key": key,
                "value": value,
                "timeAlive": timeAlive
            }
        }
        return self.__sendMessage(request)

    def clean(self, name=""):
        request = {
            "operation": "CLEAN",
            "data": {
                "tableName": name
            }
        }
        return self.__sendMessage(request)

    def remove(self, key, name=""):
        request = {
            "operation": "REMOVE",
            "data": {
                "tableName": name,
                "key": key,
            }
        }
        return self.__sendMessage(request)

    def size(self, name=""):
        request = {
            "operation": "SIZE",
            "data": {
                "tableName": name
            }
        }
        return self.__sendMessage(request)
