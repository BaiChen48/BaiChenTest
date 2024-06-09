import pandas as pd
import os
from common import file_path

manual_match_order_serial_excel_path = os.path.join(file_path.excel_file_path, 'manual_match_order_serial.xlsx')

# 创建一个serial
serial = pd.Series(data=[1, 5, '11'], index=['a', 'b', 'c'], name='serial')
# 切片
s2 = serial[:2]
# 索引
s3 = serial['c']
# 修改
serial['b'] = 66
pd.DataFrame()
if __name__ == '__main__':
    # print(serial)
    # print(s2)
    # print(s3)
    print(serial.dtype)
    print(serial.index)
    print(serial.values)
    print(serial.name)
