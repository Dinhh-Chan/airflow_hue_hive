import pandas as pd
def readcsvfile(): 
    path_csv_file = '/home/dinh-chan/Documents/project/testcode/data_thptqg.csv'
    df = pd.read_csv(path_csv_file)
    df.drop(columns=['ma_ngoai_ngu'], inplace= True)
    df.columns=['sbd', 'toan', 'van', 'ngoai_ngu', 'vat_ly', 'hoa_hoc', 'sinh_hoc', 'lich_su', 'dia_ly', 'gdcd']
    return df
print(readcsvfile())    