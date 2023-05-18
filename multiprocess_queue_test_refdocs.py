import time
import random

from multiprocessing import Process, Queue, current_process, freeze_support

#
# Function run by worker processes
#

# process関数
# inputキューをイテレータで受付、workerに計算をSTOPが出るまで続ける
def worker(input, output):
    for args in iter(input.get, 'STOP'):
        print(f'args = {args}')
        result = calculate(args)
        print(f'result, args = {result},{args}' )
        output.put(result)
    #     result = calculate(func, args)
    #     output.put(result)
    
#
# Function used to calculate result
#

# 
def calculate(args):
    result = mul(*args)
    print(f'current process = {current_process().name}')
    return '%s says that %s = %s' % (current_process().name, args, result)

#
# Functions referenced by tasks
#

def mul(a, b):
    time.sleep(0.5*random.random())
    return a * b

def plus(a, b):
    time.sleep(0.5*random.random())
    return a + b


def test():
    NUMBER_OF_PROCESSES = 4
    args_list = [(i, 7) for i in range(20)]
   

    # Create queues
    task_queue = Queue()
    done_queue = Queue()

    # Submit tasks
    for task in args_list:
        task_queue.put(task)

    # Start worker processes
    for i in range(NUMBER_OF_PROCESSES):
        Process(target=worker, args=(task_queue, done_queue)).start()

    # Get and print results
    print('Unordered results:')
    for i in range(len(args_list)):
        print('\t', done_queue.get())

    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')


if __name__ == '__main__':
    # エラーが出ない場合はfreeze_support()を無くしても
    freeze_support()
    
    test()