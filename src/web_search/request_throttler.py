import time
import asyncio

from async_util import get_lock

class RequestThrottler:
    """The purpose of this class is to limit requests to search engines"""

    def __init__(self, name: str, interval_between_requests=1):
        self.next_available_time = 0
        self.interval_between_requests = interval_between_requests
        self.lock = get_lock()
        self.name = name

    async def throttle_request(self, message:str = None):
        """This method waits until the next available time to make a request"""
        async with self.lock:  # acquire the lock
            now = time.time()
            if self.next_available_time > now:
                timeout = self.next_available_time - now
                await asyncio.sleep(timeout)
            self.next_available_time = time.time() + self.interval_between_requests
            if message:
                print(f"{self.name}: {message}")
            else:
                print(f"Performing {self.name} request")

