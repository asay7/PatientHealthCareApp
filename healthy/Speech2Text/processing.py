import concurrent.futures as cf
import time

import numpy as np


def task(sec) -> str:
    # print(f'Going to sleep...')
    time.sleep(sec)
    return f'slept for {sec}s'


def compute(N):
    for i in range(0, N):
        res = ((res * N * 1000 * i**2)**3) % 10000
    return res


def thread_exec(payload=[]):
    start = time.perf_counter()
    with cf.ThreadPoolExecutor() as cfex:
        results = cfex.map(task, payload)
    stop = time.perf_counter()
    total = round((stop - start), 2)
    print(f'Finished Threads in {total} seconds')
    return total


def multi_exec(payload=[]):
    start = time.perf_counter()
    with cf.ProcessPoolExecutor() as cfex:
        results = cfex.map(task, payload)
    stop = time.perf_counter()
    total = round((stop - start), 2)
    print(f'Finished Multi in {total} seconds')
    return total