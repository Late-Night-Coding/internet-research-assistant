import asyncio
import os
import sys

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

event_loop = asyncio.get_event_loop()

def get_event_loop():
    return event_loop

def get_lock():
    if sys.version_info <= (3,9):
        # This is required for multi-threaded async locks to work correctly in Python version 3.9 or earlier
        return asyncio.Lock(loop=event_loop)
    else:
        return asyncio.Lock()