import os

def convert_txt_to_m(directory):
    # 获取目录中的所有文件
    file_list = os.listdir(directory)

    # 遍历文件列表
    for filename in file_list:
        # 检查文件扩展名是否为.txt
        if filename.endswith(".txt"):
            # 构建.txt文件的完整路径
            txt_file = os.path.join(directory, filename)

            # 构建.m文件的完整路径
            m_file = os.path.join(directory, os.path.splitext(filename)[0] + ".m")

            # 读取.txt文件内容
            with open(txt_file, "r", encoding="UTF-8") as txt:
                content = txt.read()

            # 将内容写入.m文件
            with open(m_file, "w") as m:
                m.write(content)

            print(f"转换文件: {txt_file} -> {m_file}")

# 调用函数将指定目录中的所有.txt文件转换为.m文件
convert_txt_to_m(r"C:\Users\86138\Desktop\代码\机器学习\神经网络\遗传算法优化的神经网络")