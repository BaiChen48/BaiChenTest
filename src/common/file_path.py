import os

# 当前文件路径
current_file_path = os.path.abspath(__file__)

# 项目路径
project_path = os.path.dirname(os.path.dirname(current_file_path))

# csv文件路径
csv_file_path = os.path.join(project_path, 'Data', 'CSV')
# excel文件路径
excel_file_path = os.path.join(project_path, 'Data', 'Excel')
if __name__ == '__main__':
    print(current_file_path)
    print(project_path)
    print(csv_file_path)
    print(excel_file_path)
