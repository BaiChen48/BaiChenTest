import pyodbc
import time
# 数据库连接信息
server = '192.168.3.71'
database = 'baichentest'
username = 'sa'
password = '123456'
driver = '{ODBC Driver 17 for SQL Server}'

# 构建连接字符串
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
starttime = time.time()
# 建立数据库连接
conn = pyodbc.connect(connection_string)

try:
    # 创建游标对象
    cursor = conn.cursor()

    # 执行 SQL 查询
    query = "SELECT * FROM test"
    cursor.execute(query)

    # 获取所有查询结果
    rows = cursor.fetchall()
    for row in rows:
        print(row)  # 根据需要处理每一行数据

finally:
    # 关闭游标和连接
    cursor.close()
    conn.close()
endttime = time.time()
print(endttime-starttime)