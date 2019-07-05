"""Client for load testing servers
"""
import concurrent.futures

import requests


def do_task():
    res = requests.get('http://localhost:4000/ping')
    print(res.text)

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        print('> submitting tasks')
        pending_futures = []
        for i in range(8):
            future = executor.submit(do_task)
            pending_futures.append(future)
        print('> done task submits')
        # We use as_completed to help us grab futures as they complete / fail
        # and print their results
        for complete_future in concurrent.futures.as_completed(pending_futures):
            print('task complete after %s: ' % complete_future.result())

if __name__ == '__main__':
    main()
