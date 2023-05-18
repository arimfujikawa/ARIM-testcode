import numpy as np

# import os
# os.environ["OMP_NUM_THREADS"] = "1"
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
# os.environ["MKL_NUM_THREADS"] = "1"
# os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
# os.environ["NUMEXPR_NUM_THREADS"] = "1"


def wrap_calc(args):
    # print(args)
    return calc(*args)

def calc(A, n):

    a = np.random.random((n, n))

    b = np.random.random((n, n))
    c = np.dot(a, b).reshape([n*n])

    g = [gauss(i, a=A, mu=n*n/2, sigma=n*n/8) for i in range(n*n)]

    # ガウシアンとのコンボリューション
    conv =  np.convolve(c, g, mode='same')
    
    # x軸の定義
    x =  np.array([i for i in range(n*n)])
    from collections import defaultdict
    d = defaultdict(lambda:0)
    #4次関数でのフィッティング
    f1, f2, f3, f4, f5 = np.polyfit(x, conv, 4)
    # ここでMaybeEncodingError: Error sending result: '(0.0, defaultdict(. at 0x0000020459878720>, {}), 0.0, 0.0, 0.0, 0.0)'. Reason: 'AttributeError("Can't pickle local object 'calc..'")'
    return  f1, d, f2, f3, f4, f5
    

def gauss(x, a=1, mu=0, sigma=1):
    return a * np.exp(-(x - mu)**2 / (2*sigma**2))





# def func(x, f1, f2, f3, f4, f5):
#     return f1*x**4+f2*x**3+f3*x**2+f4*x+f5

print(wrap_calc((2,300)))