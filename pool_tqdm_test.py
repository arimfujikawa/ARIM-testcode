# Ref. https://qiita.com/nkato_/items/9e2c75013d44050851ed

from time import sleep
import random
from tqdm import tqdm
from multiprocessing import Pool, freeze_support, RLock

L = 8


def long_time_process(p):
    info = f'#{p:>2} '  # 進捗バーの左側に表示される文字列
    for _ in tqdm(range(20), desc=info, position=p+1):
        sleep(random.random())
    return p * 2


if __name__ == '__main__':
    freeze_support()  # Windows のみ必要
    with Pool(L,
             # Windows のみ必要
             initializer=tqdm.set_lock, initargs=(RLock(),)) as p:
             result = p.map(long_time_process, range(L))
    print("\n" * L)  # tqdm終了後のカーソル位置を最下部に持ってくる
    print(result)