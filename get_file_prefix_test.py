import os
import glob
import re


def get_prefix(data_number_index, file_name):
    # ファイルの接頭文字列の取得
    pattern ="^("
    for i in range(data_number_index):
        if i == data_number_index - 1:
            pattern += "[\\D]+)[\\d]+"
        else:
            pattern += "[\\D]*[\\d]+" 
    print(f'pattern = {pattern}')
    results = re.search(pattern, file_name, re.ASCII)
    return results.group(1)

# カレントディレクトリ
print(os.getcwd())

# ディレクトリのリスト
print(os.listdir())

directory = 'xafs_data'
prefix = 'pd'
extension = '.dat'
# ファイル名のリストc
uninspected_files = glob.glob(f'.\\{directory}\\*{extension}*')
# filelist = glob.glob(f'{savefileD}/{fileP}*{fileE}*')
print(uninspected_files)

# ソート
uninspected_files.sort() 
print(uninspected_files)

# 必要ないデータがないか検査
# 検査後のデータセット
files = []

# ひとつ前のファイル名と数値情報
previous_name = ''
previous_values = []
# 有効なファイル数のカウント
count = 0
# ファイル名に使用されている数値で連番になっている数値の先頭からのカウント
index = 0

for file in uninspected_files:
    name = os.path.basename(file)
    # ファイル名の長さで別のファイルを排除
    # TODO:ファイルを削除するか検討
    print(f'name = {name}')
    if 'feff' in name:
        pass
    elif '.dat' in name:
        if len(previous_name) == 0:
            pass

        elif len(name) == len(previous_name):
            count += 1

            # ファイル名の数値情報を取得
            # ".dat"をファイル名から削除後、"."を"_"に変換
            removed_extension_name = name.replace('.dat', '').replace('.', '_')
            print(f'removed_extension_name = {removed_extension_name}')
            results = re.finditer('(\d+)+?', removed_extension_name, re.ASCII)
            
            # 有効なファイルの初めの2つから連番に係る数値の前からの順番とファイルの接頭文字列を取得する
            
            if count <= 2:
                values = []
                try:
                    for i, result in enumerate(results):
                        print(f'{i}:{result.group()}')
                        values.append(result.group())

                    if len(previous_values) == 0:
                        previous_values = values
                    else:
                        for i, (previous, current) in enumerate(zip(previous_values, values)):
                            if previous == current:
                                pass
                            else:
                                print(f'{i}: {current}')
                                index = i + 1
                        previous_values = values
                        
                    # 二つ目のファイルから接頭文字列を取得する
                    if count == 2:
                        prefix = get_prefix(index, name)
                        print(f'prefix = {prefix}')
                except Exception as e:
                    print(f'error: {name} or {previous_name} is duplicated or belong difference dataset or something.')
                    exit()
                    
            else:
                pass
            
        # ひとつ前のファイル名を保存
        previous_name = name
        
            # # 連番が検出できないファイルを排除
            # # TODO:ファイルを削除するか検討
            # if results is None:
            #     print(f'warning: read data failure, {name}')
            # else:
            #     print(f'file, group = {name}, {(results)}')
            #     value = results.group(1)
            #     print(value)
            #     # 連番の重複ファイルは
            #     # TODO:ファイルを削除するか検討
            #     if value > previous_value:
            #         previous_value = value
            #         print(f'Enterd previous value = {previous_value}')
            #         files.append(file)
                    
            #     else:
            #         print(f'warning: data duplication, {name} or {previous_name}')

        