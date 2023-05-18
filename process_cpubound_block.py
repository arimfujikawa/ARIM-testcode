import numpy as np
import logging

# # prevent over-subscription of cpu
# import os
# os.environ["OMP_NUM_THREADS"] = "1"
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
# os.environ["MKL_NUM_THREADS"] = "1"
# os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
# os.environ["NUMEXPR_NUM_THREADS"] = "1"


# ロガーの生成
logger = logging.getLogger('mylog')
# 出力レベルの設定
logger.setLevel(logging.DEBUG)
# ハンドラの生成
handler = logging.FileHandler('mylog.log')
# ロガーにハンドラを登録
logger.addHandler(handler)
# フォーマッタの生成
fmt = logging.Formatter('%(asctime)s %(message)s')
# ハンドラにフォーマッタを登録
handler.setFormatter(fmt)
 

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
        logger.debug(f'results{A} = {results}')
    return results
    # fit = [func(i, f1, f2, f3, f4, f5) for i in x]

def gauss(x, a=1, mu=0, sigma=1):
    return a * np.exp(-(x - mu)**2 / (2*sigma**2))

# def func(x, f1, f2, f3, f4, f5):
#     return f1*x**4+f2*x**3+f3*x**2+f4*x+f5

print(wrap_calc(([0, 1], 5)))