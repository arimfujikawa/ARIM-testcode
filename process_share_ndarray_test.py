from multiprocessing import Process
import os
import argparse
import numpy as np


# def f(output_array_path, shape_x, shape_y):
def f(para_path):
    # loaded_para = np.load(para_path)
    loaded_para = []
    with open(para_path, 'r') as fs:
        print(fs)
        loaded_para = fs.read().split(',')
    
    print(f'para = {loaded_para}')
    output_array_path = loaded_para[0]
    # 数値データはstringから数値にキャストする必要がある
    shape_x = int(loaded_para[1])
    shape_y = int(loaded_para[2])
    out = np.zeros((shape_x, shape_y))
    out[0, 0] = 1
    out[1, 0] = 2
    print(out)
    print(f'path = {output_array_path}')
    # 結果をnumpyのbinaryファイルで保存する
    np.save(output_array_path, out)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('arg1', help='output array path')
    # parser.add_argument('arg2', help='array shape x')
    # parser.add_argument('arg3', help='array shape y')
    parser.add_argument('arg1', help='parameter path')

    args = parser.parse_args()
    
    # p = Process(target=f, args=(args.arg1, int(args.arg2), int(args.arg3),))
    p = Process(target=f, args=(args.arg1, ))
    p.start()
    p.join()