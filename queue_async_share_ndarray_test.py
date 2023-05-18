from multiprocessing import Process, Queue
import os
import argparse
import time
import numpy as np


# def f(output_array_path, shape_x, shape_y):
def f(para_path, input_q, output_q):
    # loaded_para = np.load(para_path)
    loaded_para = []
    with open(para_path, 'r') as fs:
        print(fs)
        loaded_para = fs.read().split(',')
    
    print(f'para = {loaded_para}')
    output_array_path = loaded_para[0]
    print(f'base name = {output_array_path}')
    # 数値データはstringから数値にキャストする必要がある
    shape_x = int(loaded_para[1])
    shape_y = int(loaded_para[2])
    out = np.zeros((shape_x, shape_y))
    id = input_q.get()
    time.sleep(0.1)
    out[0, 0] = id
    out[1, 1] = id
    print(f'{id} = {out}')

    splited_path = os.path.splitext(output_array_path)
    file_name = splited_path[0]+str(id)+splited_path[1]
    print(f'path = {file_name}')
    # 結果をnumpyのbinaryファイルで保存する
    np.save(file_name, out)
    output_q.put(out, id)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('arg1', help='output array path')
    # parser.add_argument('arg2', help='array shape x')
    # parser.add_argument('arg3', help='array shape y')
    parser.add_argument('arg1', help='parameter path')
    parser.add_argument('arg2', help='times')

    args = parser.parse_args()
    
    input_q = Queue()
    output_q = Queue()
    # p = Process(target=f, args=(args.arg1, int(args.arg2), int(args.arg3),))
    # p = Process(target=f, args=(args.arg1, ))
    # p.start()
    # p.join()
    processes = []
    results = np.zeros((int(args.arg2), 2, 2))
    for i in range(int(args.arg2)):
        print(f'item={i}')
        p = Process(target=f, args=(args.arg1, input_q, output_q))
        p.start()
        input_q.put(i)
        # output_q.get()の位置をどうするか
        out = output_q.get()
        print(f'out = {out}')
        results[i, :, :] = out
        processes.append(p)

    for i, p in enumerate(processes):
        p.join()
        
    print('join done')

    print(f'results = {results}:{type(results)}')
    np.save('test.npy', results)    