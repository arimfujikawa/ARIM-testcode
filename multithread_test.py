import os
import numpy as np
import cv2
from multiprocessing import Pool, cpu_count 
from tqdm import tqdm 
from glob import glob


p = Pool(processes=cpu_count()-1)
# NumPy Arrayをsaveするフォルダ
save_base_path = 'gaussian_filtered_nparrays_multi/'
# フォルダ作成
if not os.path.exists(save_base_path):
    os.makedirs(save_base_path)

def save_npy(path):
    print(path)
    #pngデータをopencvでロード
    im = cv2.imread(path)
    #pngのファイル名をそのまま.npyファイルのファイル名にする
    file_name = path.split('/')[-1].split('.png')[0]
    save_path = save_base_path + file_name
    #全てのnpyファイルを同じフォルダに格納
    np.save(save_path, im)

path_list = glob('icopng/*.png')
print(path_list)

p.map(save_npy, path_list)

# 並列処理が終わったら閉じます
p.close()
p.join()