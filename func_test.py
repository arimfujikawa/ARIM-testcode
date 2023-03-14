import pandas as pd
import os,glob
from datetime import datetime as dt
from multiprocessing import Pool

FOLDER_PATH = './'
FILE_TYPE = '*.csv'
FILE_FORMAT = 'Report_%Y%m%d.csv'

def read_report_to_dataframe():
    # ファイルパスをリスト化
    csv_pathlist = glob.glob(FOLDER_PATH + FILE_TYPE)
    with Pool(os.cpu_count()) as p:
        df = pd.concat(p.map(read_report, csv_pathlist))
    return df 


# report読み込み
def read_report(csv_path):
    separator_list = [';',',']
    
    for sep in separator_list:
        df = pd.read_csv(filepath_or_buffer=csv_path,
                         engine='python',
                         parse_dates=[0],
                         index_col=[0],
                         skiprows=[1],
                         nrows=96,
                         sep=sep)
        # データフレームが空か確認
        if not df.empty:
            break
        print(f'df = {df}')
    return df 