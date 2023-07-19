from pymemcache.client.base import Client
from pymemcache.client.retrying import RetryingClient
from pymemcache.exceptions import MemcacheUnexpectedCloseError
from django.conf import settings

class FibCache():
    def __init__(self) -> None:
        base_client = Client((settings.MEMCACHED_HOST, settings.MEMCACHED_PORT))
        self.client = RetryingClient(
            base_client,
            attempts=3,
            retry_delay=0.01,
            retry_for=[MemcacheUnexpectedCloseError]
        )

    def get(self, num):
        return self.client.get(str(num))
    
    def set(self, num, value):
        self.client.set(str(num), value)