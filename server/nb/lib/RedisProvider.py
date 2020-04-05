

import redis
from datetime import timedelta

class RedisProvider():
    def __init__(self):
        self.redis=None

    def connect(self,host,port):
        self.redis=redis.Redis( host=host, port=port)

    def read(self,param):
        return self.redis.get(param)

    def write(self,param,value):
        self.redis.setex(
            param,
            timedelta(minutes=1),
            value=value
        )




