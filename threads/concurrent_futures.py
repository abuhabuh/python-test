"""Threadpool executor example that sends a bunch of tasks to a pool of N workers
"""
import concurrent.futures
import time
import random


MAX_WORKERS = 10
NUM_JOBS = 40


def rand_sleep() -> float:
    """
    :return: float, how long sleep took
    """
    r = random.random()
    time.sleep(r)
    return r


def do_task() -> float:
    """
    :return: how long task took
    """
    return rand_sleep()
    

def main():
    print('=== running main')
    # We create a threadpool to handle tasks
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:    
        print('> subimtting tasks')
        pending_futures = []
        # We submit all jobs to the threadpool. Jobs that can't be handled
        # immediately are blocked. A "future" is a handle on a job that's
        # been submitted and we maintain a list of these.
        for i in range(NUM_JOBS):
            future = executor.submit(do_task)
            pending_futures.append(future)
        print('> done task submits')
        # We use as_completed to help us grab futures as they complete / fail
        # and print their results
        for complete_future in concurrent.futures.as_completed(pending_futures):
            print('task complete after %s: ' % complete_future.result())


if __name__ == '__main__':
    main()
