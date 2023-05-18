import numpy as np
import os
import time

# import os
# os.environ["OMP_NUM_THREADS"] = "1"
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
# os.environ["MKL_NUM_THREADS"] = "1"
# os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
# os.environ["NUMEXPR_NUM_THREADS"] = "1"

SAVE_DIRECTORY = './iobound_test'


def wrap_calc(args):
    # print(args)
    return calc(*args)

def calc(A, n):
    start = time.time()
    a = np.random.random((n, n))
    # print(f'make array = {time.time()-start}')
    np.savetxt(os.path.join(SAVE_DIRECTORY, f'iobound{A}.txt'), a)
    # print(f'save array = {time.time()-start}')

    return A

print(wrap_calc((1,1000)))