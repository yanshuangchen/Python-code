import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

import read_data

#设置中文字符的字体
font1 = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=12)
font2 = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=8)

#绘制柱形图
fig, axs = plt.subplots()
x = np.arange(len(read_data.my_list))
width = 0.25
rects1 = axs.bar(x-width, read_data.yuwen, width, label='语文')
rects2 = axs.bar(x, read_data.shuxue, width, label='数学')
rects3 = axs.bar(x+width, read_data.yingyu, width, label='英语')
axs.set_xticks(x)
axs.set_xticklabels(read_data.my_list, fontproperties=font1)
axs.set_title('成绩柱形图',fontproperties=font1)
axs.set_xlabel('姓名',fontproperties=font1)
axs.set_ylabel('分数',fontproperties=font1)
axs.legend(prop=font2)

#显示图形
plt.show()