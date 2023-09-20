import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from imageio import imread
txt=open(r"C:\Users\86138\Desktop\1.txt","r",encoding="utf-8").read()
words=jieba.lcut(txt)
excludes={'，','、','。','的','和',' ','是'}
counts={}
for word in words:
    rword=word
    counts[word]=counts.get(rword,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
pic = imread(r"C:\Users\86138\Desktop\love.png")
wc=WordCloud(mask=pic,font_path='Aa半糖奶咖.ttf',  #中文字体，须修改路径和字体名
             background_color='white', #设置背景颜色
             max_words=130,           #设置最大词数
             max_font_size=150,     #设置字体最大值
             min_font_size=40,     #设置字体最大值
             random_state=50,       #设置有多少种随机生成状态，即有多少种配色方案
             scale=1)
wc.generate_from_frequencies(counts)
plt.imshow(wc)
plt.show()

