import threading
import time
from .cache import Cache
from ..utils.common import Common


class BackgroundTasks(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = False
        self.isRunning = True

    def stop(self):
        self.isRunning = False

    def processItems(self, key, items):
        if len(items) == 0:
            return
        currentDatetime = Common.getCurrentDateAsMillis()
        for item in items:
            timeAlive = item["timeAlive"]
            if timeAlive > 0:
                createAt = item["createAt"] + timeAlive
                if currentDatetime > createAt:
                    Cache._CACHE[key].remove(item)

    def run(self, *args, **kwargs):
        while self.isRunning == True:
            try:
                for key in Cache._CACHE.keys():
                    items = Cache._CACHE[key]
                    self.processItems(key, items)
                    time.sleep(60)
            except:
                pass
