import os

def generate_txt_files(directory, num_files):
    # 创建目录（如果不存在）
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 生成指定数量的.txt文件
    for i in range(num_files):
        # 构建文件名
        filename = os.path.join(directory, f"ex{i+1}.txt")

        # 打开文件并写入内容
        with open(filename, "w") as file:
            file.write("")  # 修改为你想要的内容

        print(f"生成文件: {filename}")

# 调用函数生成10个.txt文件到指定目录
generate_txt_files(r"C:\Users\86138\Desktop\代码\机器学习\神经网络\遗传算法优化的神经网络", 10)