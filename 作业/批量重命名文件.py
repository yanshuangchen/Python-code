import os
folder_path =r"C:\Users\86138\Desktop\PNG免扣素材-服装" # 指定文件夹路径
file_names = os.listdir(folder_path)  # 获取文件夹中的所有文件名
for i, old_name in enumerate(file_names):
    new_name = f"服装素材{i+1}.jpg"  # 新文件名
    os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))