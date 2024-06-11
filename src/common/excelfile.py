from src.common.file_path import excel_file_path
import os
import pandas as pd

def read_excel_as_dataframe(file_name,):
    file_path = os.path.join(excel_file_path,file_name)
    excel_pd = pd.read_excel(file_path)
    # print(excel_pd)
    # print(excel_pd.iloc[0,0])
    # print(excel_pd.head())
    # print(excel_pd.tail())

    b = excel_pd.iloc[::, 0]
    print(b)
    # print(excel_pd.columns)
    # for i in excel_pd.columns:
    #     print(i)
if __name__ == '__main__':
    name = 'manual_match_order_serial.xlsx'
    read_excel_as_dataframe(name)