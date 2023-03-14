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

    global results
    #PILでロード
    im = Image.open(args[0][1]).convert('L')
    
    # results[args[0][0]] = lambda a=args[0][0]: a*2
    print(im.getpixel((20, 20)))
    im = np.array(im)
    im = im.astype(np.float64)
    num = 6
    im_b = im
    for _ in range(num):
        im_a = im+np.var(im)
        im_b = im-np.var(im_b)
        im = np.cov(im_b, im_a)

    x = np.argsort(im.flatten())
    y = np.argsort(x)
    results[args[0][0]] = args[0][0]
    print(results)

    return args[0][0],args[0][1]



