# multiprocessing.Process, Queueのプロセス間通信によるマルチプロセス

import time
import random
import argparse
from multiprocessing import Process, Queue, current_process, freeze_support, cpu_count
import logging
logging.basicConfig(filename = f'subprocess_queue.log', encoding='utf-8', level=logging.DEBUG)
#
# Function run by worker processes
#

# process関数
# inputキューをイテレータで受付、workerに計算をSTOPが出るまで続けるか（公式Doc）
# whileで待って適当なキー（None等）でbreakする
def worker(input, output):
    while True:
        args = input.get()
        if args is None:
            break
        # print(f'args = {args}')
        result = calculate(args)
        # print(f'result, args = {result},{args}' )
        calc()
        output.put(result)
    # output.close()
#
# Function used to calculate result
#
# 
def calculate(args):
    result = mul(*args)
    # print(f'current process = {current_process().name}')
    return '%s says that %s = %s' % (current_process().name, args, result)

def calc():
    n = 5000
    a = [[i for i in range(n) ] for _ in range(n)]
    b = []
    for x in a:
        c = []
        for y in x:
            c.append(y*2)
        b.append(c)
#
# Functions referenced by tasks
#

def mul(a, b):
    time.sleep(0.5*random.random())
    # return a * b
    # return int(a) * b

    return int(a) * b[0]

def plus(a, b):
    time.sleep(0.5*random.random())
    return a + b


def test(number_core):
    # n = 10
    # NUMBER_OF_PROCESSES = cpu_count()-1 # 17. sec
    # NUMBER_OF_PROCESSES = 10 # 13.1 sec
    # NUMBER_OF_PROCESSES = 9 # 14.6 sec
    # NUMBER_OF_PROCESSES = 8 # 8.8 sec
    # NUMBER_OF_PROCESSES = 7 # 8.3 sec
    # NUMBER_OF_PROCESSES = 6 # 8.3 sec
    # NUMBER_OF_PROCESSES = 5 # 8.4 sec
    # NUMBER_OF_PROCESSES = 4 # 10.3 sec
    # NUMBER_OF_PROCESSES = 3 # 12.2 sec
    # NUMBER_OF_PROCESSES = 2 # 14.3 sec
    # NUMBER_OF_PROCESSES = 1 # 26.0 sec
    # n= 5
    # NUMBER_OF_PROCESSES = cpu_count()-1 # 4.2 sec
    # NUMBER_OF_PROCESSES = 10 # 4.0 sec
    # NUMBER_OF_PROCESSES = 9 # 4.3 sec
    # NUMBER_OF_PROCESSES = 8 # 4.1 sec
    # NUMBER_OF_PROCESSES = 7 # 4.2 sec
    # NUMBER_OF_PROCESSES = 6 # 4.1 sec
    # NUMBER_OF_PROCESSES = 5 # 4.2 sec
    # NUMBER_OF_PROCESSES = 4 # 6.0 sec
    # NUMBER_OF_PROCESSES = 3 # 6.2 sec
    # NUMBER_OF_PROCESSES = 2 # 8.4 sec
    # NUMBER_OF_PROCESSES = 1 # 12.6 sec
    # n = 20
    # NUMBER_OF_PROCESSES=1 takes 51.848055362701416 sec
    # NUMBER_OF_PROCESSES=2 takes 32.51121401786804 sec
    # NUMBER_OF_PROCESSES=3 takes 24.072312355041504 sec
    # NUMBER_OF_PROCESSES=4 takes 18.779661655426025 sec
    # NUMBER_OF_PROCESSES=5 takes 15.853334903717041 sec
    # NUMBER_OF_PROCESSES=6 takes 16.804600715637207 sec
    # NUMBER_OF_PROCESSES=7 takes 17.528395891189575 sec
    # NUMBER_OF_PROCESSES=8 takes 19.066620588302612 sec
    # NUMBER_OF_PROCESSES=9 takes 18.459457635879517 sec
    # NUMBER_OF_PROCESSES=10 takes 20.47127103805542 sec
    # NUMBER_OF_PROCESSES=11 takes 32.96067833900452 sec
    # n = 15
    # NUMBER_OF_PROCESSES=1 takes 39.3792200088501 sec
    # NUMBER_OF_PROCESSES=2 takes 25.70305037498474 sec
    # NUMBER_OF_PROCESSES=3 takes 16.832674026489258 sec
    # NUMBER_OF_PROCESSES=4 takes 14.322266578674316 sec
    # NUMBER_OF_PROCESSES=5 takes 12.202588081359863 sec
    # NUMBER_OF_PROCESSES=6 takes 12.399075031280518 sec
    # NUMBER_OF_PROCESSES=7 takes 12.263251781463623 sec
    # NUMBER_OF_PROCESSES=8 takes 13.898592710494995 sec
    # NUMBER_OF_PROCESSES=9 takes 13.618212223052979 sec
    # NUMBER_OF_PROCESSES=10 takes 15.80559515953064 sec
    # NUMBER_OF_PROCESSES=11 takes 19.957395553588867 sec
    #
    # coreの数は5-7がよさそう
    #
    
    # n = 3 計算数が少ないとコアを増やしても意味がない
    # NUMBER_OF_PROCESSES=1 takes 7.499591588973999 sec
    # NUMBER_OF_PROCESSES=2 takes 5.645368814468384 sec
    # NUMBER_OF_PROCESSES=3 takes 3.480245351791382 sec
    # NUMBER_OF_PROCESSES=4 takes 3.2951290607452393 sec
    # NUMBER_OF_PROCESSES=5 takes 3.237330198287964 sec
    # NUMBER_OF_PROCESSES=6 takes 3.293283462524414 sec
    # NUMBER_OF_PROCESSES=7 takes 3.2831292152404785 sec
    # NUMBER_OF_PROCESSES=8 takes 3.6352415084838867 sec
    # NUMBER_OF_PROCESSES=9 takes 3.7116377353668213 sec
    # NUMBER_OF_PROCESSES=10 takes 3.2400424480438232 sec
    # NUMBER_OF_PROCESSES=11 takes 3.3117754459381104 sec
    
    
    # print(f'number of core = {NUMBER_OF_PROCESSES}')

    n = 3
    # args_list = [(i, 7) for i in range(n)]
    args_list = [(str(i), 7) for i in range(n)]
    args_list = [(str(i), (7, 'test')) for i in range(n)]


    # args_list = [(1, 7)]

    # Create queues
    task_queue = Queue()
    done_queue = Queue()

    # Submit tasks
    for task in args_list:
        task_queue.put(task)
        logging.info(task_queue)

    # Start worker processes
    # for i in range(NUMBER_OF_PROCESSES):
    for i in range(number_core):

        Process(target=worker, args=(task_queue, done_queue)).start()
        logging.info(f'task{i} starts')
    logging.info('try to get results')
    # Get and print results
    # print('Unordered results:')
    for i in range(len(args_list)):
        logging.info(f'{i} get')
        result = done_queue.get()
        # print('\t', result)

    # Tell child processes to stop
    # for i in range(NUMBER_OF_PROCESSES):
    for i in range(number_core):

        task_queue.put(None)


if __name__ == '__main__':
    # エラーが出ない場合はfreeze_support()を無くしても
    freeze_support()
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='number of core')
    args = parser.parse_args()
    core_count = int(args.arg1)
    
    for core_number in range(1, core_count+1):
        start_time = time.time()
        test(core_number)
        logging.info(f'NUMBER_OF_PROCESSES={core_number} takes {time.time()-start_time} sec')