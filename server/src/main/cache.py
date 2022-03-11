import sys
import datetime
from ..utils.common import Common
class Cache(object):
    _MICRO_TO_MILLIS = 1_000_000
    _CACHE = dict()

    def __init__(self, maxLenInBytes = 0, timeAlive = 0):
        self.maxLenInBytes = maxLenInBytes
        self.timeAlive = timeAlive

    def ckeckSize(self):
        if self.maxLenInBytes > 0:
            size = Cache._CACHE.__sizeof__() or sys.getsizeof(Cache._CACHE)
            if size > self.maxLenInBytes:
                raise Exception("outsized")

    def set(self, key, value, timeAlive=None, name="ALL") -> None:
        startTime = datetime.datetime.now()
        if not timeAlive: timeAlive = self.timeAlive
        if not name: name = "ALL"
        output = {
            "name": name,
            "operation": "SET",
            "data": None
        }
        try:
            self.ckeckSize()
            if name not in Cache._CACHE:
                Cache._CACHE[name] = []
            items = Cache._CACHE[name]
            item = { "key": key, "value": value, "createAt": Common.getCurrentDateAsMillis(), "timeAlive": timeAlive }
            if len(items) > 0:
                index = -1
                for i in range(len(items)):
                    if items[i]["key"] == key:
                        index = i
                        break
                if index > -1:
                    items[index] = item
                else:
                    items.append(item)
            else:
                items.append(item)
            output["data"] = item["value"]
            return output
        except Exception as e:
            raise e
        finally:
            endTime = datetime.datetime.now()
            delta = endTime - startTime
            output["responseTime"] = delta.microseconds / Cache._MICRO_TO_MILLIS

    def get(self, key, name="ALL") -> any:
        startTime = datetime.datetime.now()
        if not name: name = "ALL"
        output = {
            "name": name,
            "operation": "GET",
            "data": None
        }
        try:
            if name not in Cache._CACHE:
                return output
            items = Cache._CACHE[name]
            if not items:
                return output
            for item in items:
                if item["key"] == key:
                    output["data"] = item["value"]
                    break
            return output
        except Exception as e:
            raise e
        finally:
            endTime = datetime.datetime.now()
            delta = endTime - startTime
            output["responseTime"] = delta.microseconds / Cache._MICRO_TO_MILLIS

    def getAll(self, name="ALL") -> any:
        startTime = datetime.datetime.now()
        if not name: name = "ALL"
        output = {
            "name": name,
            "operation": "GET_ALL",
            "data": None
        }
        try:
            if name not in Cache._CACHE:
                return output
            output["data"] = Cache._CACHE[name]
            return output
        except Exception as e:
            raise e
        finally:
            endTime = datetime.datetime.now()
            delta = endTime - startTime
            output["responseTime"] = delta.microseconds / Cache._MICRO_TO_MILLIS

    def remove(self, key, name="ALL") -> None:
        startTime = datetime.datetime.now()
        if not name: name = "ALL"
        output = {
            "name": name,
            "operation": "REMOVE",
            "data": None
        }
        try:
            if name not in Cache._CACHE:
                return output
            items = Cache._CACHE[name]
            if not items:
                return output
            index = -1
            for i in range(len(items)):
                if items[i]["key"] == key:
                    index = i
                    break
            if index >= 0:
                output["data"] = items[index]["value"]
                items.remove(items[index])
            return output
        except Exception as e:
            raise e
        finally:
            endTime = datetime.datetime.now()
            delta = endTime - startTime
            output["responseTime"] = delta.microseconds / Cache._MICRO_TO_MILLIS
    
    def size(self, name = None):
        startTime = datetime.datetime.now()
        if not name: name = "ALL"
        output = {
            "name": name,
            "operation": "SIZE",
            "data": None
        }
        try:
            total = 0
            if name and name in Cache._CACHE:
                total += len(Cache._CACHE[name])
                output["data"] = total
            else:
                for key in Cache._CACHE.keys():
                    total += len(Cache._CACHE[key])
                    output["data"] = total
            return output
        except Exception as e:
            raise e
        finally:
            endTime = datetime.datetime.now()
            delta = endTime - startTime
            output["responseTime"] = delta.microseconds / Cache._MICRO_TO_MILLIS

    def clean(self, name = None):
        startTime = datetime.datetime.now()
        if not name: name = "ALL"
        output = {
            "name": name,
            "operation": "CLEAN",
            "data": None
        }
        try:
            if name and name in Cache._CACHE:
                Cache._CACHE[name] = []
            else:
                for key in Cache._CACHE.keys():
                    del Cache._CACHE[key]
                Cache._CACHE = dict()
            return output
        except Exception as e:
            raise e
        finally:
            endTime = datetime.datetime.now()
            delta = endTime - startTime
            output["responseTime"] = delta.microseconds / Cache._MICRO_TO_MILLIS

if __name__ == '__main__':
    try:
        cache = Cache(1000)
        for i in range(1000):
            key = "key"+str(i)
            cache.set(key, i)
        cont = 0
        maxTime = 0
        for i in range(1000):
            key = "key"+str(i)
            response = cache.get(key)
            if response["responseTime"] > 0:
                cont += 1
            if response["responseTime"] > maxTime:
                maxTime = response["responseTime"]
        print(cont, maxTime)
    except KeyboardInterrupt as e:
        sys.exit(0)
    except Exception as e:
        sys.exit(0)