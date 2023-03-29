from multiprocessing import Process, Value, Array, Queue

# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         print(a[:])
#         a[i] = -a[i]

def f(input_q, a):
    item = input_q.get()
    print(item)
    a[item] = item*2

if __name__ == '__main__':
    input_q = Queue()
    arr = Array('i', range(10))
    max_worker = len(arr)
    processes = []
    
    for _ in range(len(arr)):
        p = Process(target=f, args=(input_q, arr))
        p.start()
        processes.append(p)
    for i in range(len(arr)):
        input_q.put(i)
    
    for p in processes:
        p.join()


    print(f'final arr = {arr[:]}')