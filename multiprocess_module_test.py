import os
import numpy as np
import cv2
from multiprocessing import Pool, cpu_count 
from tqdm import tqdm 
from glob import glob
save_base_path = 'gaussian_filtered_nparrays_multi/'

def save_npy(path):
    save_base_path = 'gaussian_filtered_nparrays_multi/'
    print(path)
    #pngデータをopencvでロード
    im = cv2.imread(path)
    #pngのファイル名をそのまま.npyファイルのファイル名にする
    file_name = path.split('/')[-1].split('.png')[0]
    save_path = os.path.join(save_base_path, file_name)
    #全てのnpyファイルを同じフォルダに格納
    np.save(save_path, im)
    return path


if __name__ == '__main__':
    p = Pool(processes=cpu_count()-1)
    # NumPy Arrayを saveするフォルダ
    # フォルダ作成
    icon_directory = 'icopng/'
    
    save_directory = os.path.join(save_base_path, icon_directory)
    print(f'save directory = {save_directory}')
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    icon_glob_item = os.path.join(icon_directory, '*.png')
    print(f'icon glob item = {icon_glob_item}')

    path_list = glob(icon_glob_item)
    print(f'path list = {path_list}')
    results = []

    for result in p.map(save_npy, path_list):
        print(result)
     

   
   