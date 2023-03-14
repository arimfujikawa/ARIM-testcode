import os
from multiprocessing import Pool
from glob import glob
from PIL import Image
# import cv2
import numpy as np
i = 0

save_base_path = 'gaussian_filtered_nparrays/'
path_list = glob('icopng/*.png')
print(path_list)
results = [0 for _ in range(len(path_list))]
numbers = [i for i in range(len(path_list))]
map_list = [[i, path] for i, path in enumerate(path_list)]

# def thread_save(path):
#     global save_base_path
#     with save_im(path, save_base_path) as thread:
#         return path
def thread_save():
    with Pool(os.cpu_count()-1) as p:
        p.map(save_im, map_list) 
        
# with Pool(os.cpu_count()) as p:
#         df = pd.concat(p.map(read_report, csv_pathlist))
#     return df 

def save_im(*args):
    global save_base_path
    global results
    #PILでロード
    im = Image.open(args[0][1]).convert('L')
    results[args[0][0]] = lambda a=args[0][0]: a*2
    print(im.getpixel((20, 20)))
    im = np.array(im)
    im = im.astype(np.float64)
    #pngデータをopencvでロード
    # im_cv = cv2.imread(p)
    # pil_img = Image.fromattay(im_cv)
    #pngのファイル名をそのまま.npyファイルのファイル名にする
    file_name = os.path.basename(args[0][1])
    print(file_name)
    save_path = save_base_path + file_name.split('.')[0]
    print(save_path)
    # results[args[0][0]] = args[0][0]
    print(results)
    #全てのnpyファイルを同じフォルダに格納
    np.savetxt(save_path, im)

