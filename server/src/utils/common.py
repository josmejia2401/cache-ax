import datetime
class Common(object):
    @staticmethod
    def getCurrentDateAsMillis():
        return round(datetime.datetime.utcnow().timestamp() * 1000)
