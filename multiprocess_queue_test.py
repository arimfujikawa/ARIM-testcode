
import numpy as np
import cv2
from multiprocessing import Pool, cpu_count 
import sys
from PIL import Image
import time
save_base_path = 'gaussian_filtered_nparrays/'

# 結果保存用のリストを初期化
results = [[0, 0] for _ in range(11)]

# 引数をリストで受け取るラッパー


#　実際のprocess処理
def save_npy(q, path):
    global results
    while True:
        item = q.get()
        if item is None:
            break
        # 処理のため少しディレイを入れる
        time.sleep(0.1)
        
        # pngデータをopencvでロード
        im = cv2.imread(path)
        # わざとCPUバウンドの処理を入れる
        im_calc = Image.open(path).convert('L')
        im_calc = np.array(im)
        im_calc = im_calc.astype(np.float64)
        i = 6
        im_b = im_calc
        for _ in range(i):
            im_a = im_calc+np.var(im_calc)
            im_b = im_calc-np.var(im_b)
            im_calc = np.cov(im_b, im_a)
        x = np.argsort(im_calc.flatten())
        # 処理結果をglobalの結果ファイルに代入する
        results[item][0] = item
        results[item][1] = len(x)
        #pngのファイル名 + フォルダ名を.npyファイルのファイル名にする
        file_name = path.split('\\')[-1].split('.png')[0]
        save_path = save_base_path + file_name + '_' + path.split('.')[1]
        #全てのnpyファイルを同じフォルダに格納
        np.save(save_path, im)

        print(f'Finished q[{item}] = {path}')
        q.task_done()
    #pngデータをopencvでロード

    return save_path, results, item
# if __name__ == '__main__':
#     wrap_save_npy(sys.argv)
