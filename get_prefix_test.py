import re

def _get_prefix(data_number_index, file_name):
    # ファイルの接頭文字列の取得
    pattern ="^("
    for i in range(data_number_index):
        if i == data_number_index - 1:
            pattern += "[\\D]+)[\\d]+"
        else:
            pattern += "[\\D]*[\\d]+" 
            
    results = re.search(pattern, file_name, re.ASCII)
    return results.group(1)

FILE_NAME = '10ad0001.dat'

print(_get_prefix(1, FILE_NAME))