
class PathosTest:
    save_base_path = 'gaussian_filtered_nparrays/'


# 結果保存用のリストを初期化
    results = [[0, 0] for _ in range(11)]
    top_namespace = None
    def __init__(self):
        pass
# 引数をリストで受け取るラッパー
    def wrap_save_npy(self, args):
        
        print(f'wrap_save_npy top_namespace = {self.top_namespace}')
        print(f'args = {args}')
        path, type_name, num, k = args
    # print(f'name space = {namespace}')
        for name in self.top_namespace:
            print(f'{name}={self.top_namespace[name]}')
            if name == k:
                print(f'{k} exists = {self.top_namespace[k]}')
                self.top_namespace[k][0][0] = 1
                print(self.top_namespace[k])
            
        return self._save_npy(path, type_name, num, k)

#　実際のprocess処理
    def _save_npy(self, path, type_name, num, k):
        from PIL import Image
        import numpy as np
        import cv2
        #pngデータをopencvでロード
        print(f'_save_npy namespace = {self.top_namespace}')
        for name in self.top_namespace:
            print(f'{name}={self.top_namespace[name]}')
            if name == k:
                print(f'{k} exists = {self.top_namespace[k]}')
                self.top_namespace[k][0][0] = 1
                print(self.top_namespace[k])
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
        self.results[num][0] = num
        self.results[num][1] = len(x)
        self.top_namespace[k][num][0] = num
        self.top_namespace[k][num][1] = len(x)
        #pngのファイル名 + フォルダ名を.npyファイルのファイル名にする
        file_name = path.split('\\')[-1].split('.png')[0]
        save_path = self.save_base_path + file_name + '_' + type_name
        #全てのnpyファイルを同じフォルダに格納
        np.save(save_path, im)
        return save_path, self.results, num
# if __name__ == '__main__':
#     wrap_save_npy(sys.argv)
