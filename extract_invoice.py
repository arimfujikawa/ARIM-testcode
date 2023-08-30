import json
import pandas as pd

line = 0
# def make_table(data, index=0, line=0, dataframe=None):
def make_table(data, index=0, dataframe=None):

    global line
    if isinstance(data, dict):
        for key,value in data.items():
            print(f'key,value {line}:{index} = {key}, {value}')
            if len(dataframe.columns)-1 < index:
                if len(df.filter(items=[f'key{index}']).columns) == 0:
                    dataframe[f'key{index}'] = ''
            dataframe.loc[line, f'key{index}'] = key         
            # make_table(value, index+1, line, dataframe)
            make_table(value, index+1, dataframe)

            
    else:
        print(f'value {line}:{index} = {data}')
        dataframe.loc[line, 'value'] = data
        line += 1
        
    return 

json_file = 'json_file/metadata-def_test.json'
with open(json_file, 'r', encoding='utf-8') as f:
    dict_object = json.load(f)
print(dict_object)
df = pd.DataFrame()
df['value'] = ''
make_table(dict_object, dataframe=df)
print(df)
df.to_csv('dataframe.csv', mode='w', sep=',', encoding="shift jis")