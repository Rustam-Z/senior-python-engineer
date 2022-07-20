# time python3 test.py

import random
import multiprocessing

NUM_PROC = 2


def append_to_list(lst, num_items):
    """Appends num_items integers within the range [0-20000000) to the input lst"""
    for n in random.sample(range(20000000), num_items):
        lst.append(n)


if __name__ == "__main__":
    jobs = []

    for i in range(NUM_PROC):
        process = multiprocessing.Process(
            target=append_to_list,
            args=([], 10000000)
        )
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()
