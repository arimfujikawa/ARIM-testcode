from multiprocessing import Process
import os
import argparse
import numpy


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1')
    parser.add_argument('arg2')

    args = parser.parse_args()
    # info('main line')
    info(args.arg1)

    # p = Process(target=f, args=('bob',))
    p = Process(target=f, args=(args.arg2,))

    p.start()
    p.join()