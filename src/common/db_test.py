import pandas as pd
from sqlalchemy import create_engine
import time

# 示例：连接到 SQL Server
server = '192.168.3.71'
database = 'baichentest'
username = 'sa'
password = '123456'
driver = 'ODBC Driver 17 for SQL Server'  # 根据你的 ODBC 驱动调整

starttime = time.time()
print(starttime)
# 构建连接字符串
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

# 创建引擎
engine = create_engine(connection_string)
# 使用 SQL 查询读取数据
query = "SELECT * FROM test"
df = pd.read_sql_query(query, engine)
# print(df)
# 或者直接读取整个表
df = pd.read_sql_table('test', con=engine)
print(df)
endttime = time.time()
print(endttime-starttime)
engine.dispose()