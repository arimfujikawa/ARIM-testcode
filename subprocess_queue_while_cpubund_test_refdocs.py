# multiprocessing.Process, Queueのプロセス間通信によるマルチプロセス

import time
import random
import argparse
from multiprocessing import Process, Queue, current_process, freeze_support, cpu_count
import logging
logging.basicConfig(filename = f'subprocess_queue.log', encoding='utf-8', level=logging.DEBUG)
import time
import random

from multiprocessing import Process, Queue, current_process, freeze_support

#
# Function run by worker processes
#

def worker(input, output):
    # for items in iter(input.get, 'STOP'):
    while True:
        items = input.get()
        if items is None:
            break
        result = calculate(items[0], items[1])
        output.put(result)

#
# Function used to calculate result
#

def calculate(func, args):
    result = func(*args)
    return '%s says that %s%s = %s' % \
        (current_process().name, func.__name__, args, result)

#
# Functions referenced by tasks
#
def calc(a, b):
    result = mul(a, b)
    time.sleep(0.5*random.random())
    n = 5000
    a = [[i for i in range(n) ] for _ in range(n)]
    b = []
    sum = 0
    for x in a:
        c = []
        for y in x:
            c.append(y*2)
            sum += y*2
        b.append(c)
    logging.info(f'sum, result = {sum}, {result}')
    
    return sum*result


def mul(a, b):
    time.sleep(0.5*random.random())
    return a * b

def plus(a, b):
    time.sleep(0.5*random.random())
    return a + b


def test():
    NUMBER_OF_PROCESSES = 4
    logging.info(f'number of process = {NUMBER_OF_PROCESSES}')
    TASKS1 = [(calc, (i, 7)) for i in range(20)]
    TASKS2 = [(plus, (i, 8)) for i in range(10)]

    # Create queues
    task_queue = Queue()
    done_queue = Queue()

    # Submit tasks
    for task in TASKS1:
        task_queue.put(task)

    # Start worker processes
    for i in range(NUMBER_OF_PROCESSES):
        Process(target=worker, args=(task_queue, done_queue)).start()

    # Get and print results
    print('Unordered results:')
    for i in range(len(TASKS1)):
        print('\t', done_queue.get())

    # Add more tasks using `put()`
    for task in TASKS2:
        task_queue.put(task)

    # Get and print some more results
    for i in range(len(TASKS2)):
        print('\t', done_queue.get())

    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        # task_queue.put('STOP')
        task_queue.put(None)



if __name__ == '__main__':
    freeze_support()
    start = time.time()
    test()
    logging.info(f'total time = {time.time()-start}')

