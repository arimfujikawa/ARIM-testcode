from multiprocessing import Process
import os
import argparse
import numpy as np


def f(output_array_path, shape:tuple):
    out = np.zeros((shape))
    print(out)
    print(f'path = {output_array_path}')
    np.save(output_array_path, out)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='output array path')
    parser.add_argument('arg2', help='array shape:type tuple')

    args = parser.parse_args()
    
    p = Process(target=f, args=(args.arg1, args.arg2,))
    p.start()
    p.join()