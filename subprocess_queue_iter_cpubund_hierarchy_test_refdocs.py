# multiprocessing.Process, Queueのプロセス間通信によるマルチプロセス

import time
import random
import argparse
from multiprocessing import Process, Queue, current_process, freeze_support, cpu_count
import logging
logging.basicConfig(filename = f'subprocess_queue.log', encoding='utf-8', level=logging.DEBUG)
import time
import random
from datetime import datetime
import numpy as np
from multiprocessing import Process, Queue, current_process, freeze_support
logging.debug('debug on')
logging.info('info on')
#
# Function run by worker processes
#

def worker(input, output):
    for func, args in iter(input.get, 'STOP'):
        result = calculate(func, args)
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
    logging.info(f'parent process {current_process().name} start on {datetime.now().strftime("%H%M%S")}')
    result = mul(a, b)
    # logging.info(f'parent mul result = {result}')
    time.sleep(0.5*random.random())
    n = 2
    a_p_list = [[i for i in range(n) ] for _ in range(n)]
    b_p_list = []
    sum = 0
    for x in a_p_list:
        c = []
        for y in x:
            c.append(y*2)
            sum += y*2
        b_p_list.append(c)
    logging.debug(f'b_p_list = {b_p_list}')
    child_result = child_calc(a, b)
    logging.info(f'parent process {current_process().name} done on {datetime.now().strftime("%H%M%S")} = {sum}')
    ndarray_a = np.zeros((2,2))
    dict_result = {'a':a, 'b':b, 'b list':b_p_list[0], 'ndarray a':ndarray_a}
    return sum*result, child_result, ndarray_a, dict_result

def child_calc(a, b):
    logging.info(f'child process {current_process().name} start on {datetime.now().strftime("%H%M%S")}')
    result = plus(a, b)
    # logging.info(f'child plus result = {result}')
    time.sleep(0.5*random.random())
    n = 2
    a_list = [[i for i in range(n) ] for _ in range(n)]
    b_list = []
    sum = 0
    for x in a_list:
        c = []
        for y in x:
            c.append(y*2)
            sum += y
            # logging.info(f'sum = {sum}:{type(sum)}')
        b_list.append(c)
    grandchild_result = granddhild_calc(a, b)
    logging.info(f'child process {current_process().name} done on {datetime.now().strftime("%H%M%S")} = {result}')
    return sum+result/grandchild_result

def granddhild_calc(a, b):
    logging.info(f'grandchild process {current_process().name} start on {datetime.now().strftime("%H%M%S")}')
    result = plus(a, b) + mul(a, b)
    # logging.info(f'child plus result = {result}')
    time.sleep(0.5*random.random())
    n = 5000
    a_list = [[i for i in range(n) ] for _ in range(n)]
    b_list = []
    sum = 0
    for x in a_list:
        c = []
        for y in x:
            c.append(y*2)
            sum += y
            # logging.info(f'sum = {sum}:{type(sum)}')
        b_list.append(c)
    logging.info(f'grandchild process {current_process().name} done on {datetime.now().strftime("%H%M%S")} = {result}')
    return sum+result


def mul(a, b):
    # time.sleep(0.5*random.random())
    return a * b

def plus(a, b):
    # time.sleep(0.5*random.random())
    return a + b


def test():
    NUMBER_OF_PROCESSES = 8
    logging.info(f'number of process = {NUMBER_OF_PROCESSES}')
    TASKS1 = [(calc, (i, 7)) for i in range(3)]
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
        result = done_queue.get()
        logging.info(f'result = {result}')
        print(result)
        # print('\t', done_queue.get())

    # Add more tasks using `put()`
    for task in TASKS2:
        task_queue.put(task)

    # Get and print some more results
    for i in range(len(TASKS2)):
        print('\t', done_queue.get())

    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')


if __name__ == '__main__':
    freeze_support()
    start = time.time()
    test()
    logging.info(f'total time = {time.time()-start}')

