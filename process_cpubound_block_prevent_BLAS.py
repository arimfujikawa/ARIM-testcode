# # prevent over-subscription of cpu
# import os
# os.environ["OMP_NUM_THREADS"] = "1"
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
# os.environ["MKL_NUM_THREADS"] = "1"
# os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
# os.environ["NUMEXPR_NUM_THREADS"] = "1"

import numpy as np

def wrap_calc(args):
    return calc(*args)

def calc(As, n):

    results = []
    for A in As:
        a = np.random.random((n, n))
        b = np.random.random((n, n))
        c = np.dot(a, b).reshape([n*n])

        g = [gauss(i, a=A, mu=n*n/2, sigma=n*n/8) for i in range(n*n)]
        # ガウシアンとのコンボリューション
        conv =  np.convolve(c, g, mode='same')
        # x軸の定義
        x =  np.array([i for i in range(n*n)])

        #4次関数でのフィッティング
        f1, f2, f3, f4, f5 = np.polyfit(x, conv, 4)
        results.append([f1, f2, f3, f4, f5])

    return results
    # fit = [func(i, f1, f2, f3, f4, f5) for i in x]

def gauss(x, a=1, mu=0, sigma=1):
    return a * np.exp(-(x - mu)**2 / (2*sigma**2))
