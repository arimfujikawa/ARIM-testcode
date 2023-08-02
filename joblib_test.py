import time
import numpy as np
from joblib import Parallel, delayed

def countdown(n):
    while n > 0:
        n -= 1
        print(n)
    return n

CPU_COUNT = 2
TIMES = 3
N = 2

start = time.time()
for result in Parallel(n_jobs=CPU_COUNT) ([delayed(countdown) (N) for _ in range(TIMES)]):
    pass

print(time.time() - start)
