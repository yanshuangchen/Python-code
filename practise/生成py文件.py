import os

# 指定要生成文件的文件夹
folder_path = r"C:\Users\86138\Desktop\numpy"

# 指定要生成的文件数量
num_files = 20

# 循环生成文件
for i in range(1,num_files):
    # 组合文件名
    file_name = f'numpy{i}.py'
    # 拼接文件路径
    file_path = os.path.join(folder_path, file_name)
    # 创建空文件
    with open(file_path, 'w') as f:
        pass