import asyncio
import datetime
import time

import requests


async def foo():
    print(f'foo begin')
    await asyncio.sleep(1)
    print(f'foo end')

async def main():
    print(f'start: {datetime.datetime.now()}')
    await asyncio.gather(foo(),foo(),foo())
    print(f'end: {datetime.datetime.now()}')

if __name__ == '__main__':
    asyncio.run(main())
