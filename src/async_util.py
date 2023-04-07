import asyncio
import os

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

event_loop = asyncio.get_event_loop()

def get_event_loop():
    return event_loop

def get_lock():
    return asyncio.Lock(loop=event_loop)