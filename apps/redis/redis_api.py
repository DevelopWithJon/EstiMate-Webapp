import redis
from redis.commands.json.path import Path
from redis.exceptions import ConnectionError, RedisError, NoPermissionError, TimeoutError, MovedError

class RedisApi:
    
    def __init__(self, expirationTime=600):
        self.client = self._client()
        self.expirationTime = expirationTime

    def _client(self):
        """
        connect to redis instance.
        """
        try: 
            return redis.Redis(
            host='redis-16791.c14.us-east-1-3.ec2.cloud.redislabs.com',
            port=16791, 
            password='fMjphArvG5a1w03Pq4sPZb44H9BnNLZ8')
        except ConnectionError as err:
            print(err)
    
    def set(self, userId, data):
        """
        set value to memory.
        """
        try:
            self.client.json().set(str(userId), Path.root_path(), data)
            self._set_expiration(userId)
            print(f"successfully added records for user={userId}")
        except (RedisError, TimeoutError) as err:
            print(err)
    
    def get(self, userId, propertyId=None):
        """
        get value from memory.
        """
        if not propertyId:
            get_value = self.client.json().get(str(userId))
            return get_value if get_value else print(f"no such key{userId}, Either data is incorrect or record has expired")      
        propertyId = "." + str(propertyId)
        get_value = self.client.json().get(str(userId), propertyId)
        return get_value if get_value else print(f"no such key{userId}.{propertyId}, Either data is incorrect or record has expired")

    def _set_expiration(self, userId):
        """
        set key expiration.
        """
        print(f"expiration set={self.client.expire(userId, self.expirationTime)}")

    def show_all(self):
        """
        show all data
        """
        print(self.client.keys('*'))

    def flush(self):
        """
        clear data from memory.
        """
        self.client.flushall()