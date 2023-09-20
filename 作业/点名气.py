import random

# 打开名字文件
with open('names.txt') as f:
    # 读取名字列表并去除换行符
    names = [name.strip() for name in f.readlines()]

# 随机选择一个名字
random_name = random.choice(names)

# 打印选择的名字
print('The chosen name is:', random_name)
