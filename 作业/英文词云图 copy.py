#txt文件本身是utf-8编码方式的
import matplotlib.pyplot as plt
from imageio.v2 import imread
from wordcloud import WordCloud
#引用相关函数

txt = open(r"C:\Users\86138\Desktop\yinwen.txt", "r",encoding="utf-8").read( )
txt = txt.lower( )
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        #将文本中特殊字符替换为空格
    Txt = txt.replace(ch, " ")
words  = Txt.split( )
counts = { }
for word in words:			
    counts[word] = counts.get(word,0) + 1
excludes={"the","and","of","a","in",'to','it','is','as','are','not','over','for','your','and','there','by'}
for word in excludes:
       del(counts[word])
items = list(counts.items( ))
items.sort(key=lambda x:x[1], reverse=True) 
# for i in range(10):
#     word, count = items[i]
#     print ("{0:<10}{1:>5}".format(word, count))  
#0:表示第一列，<10表示左对齐    1:表示第二列，>5表示右对齐
pic = imread(r"C:\Users\86138\Desktop\love.png") #中文字体，须修改路径和字体名
wc=WordCloud(mask=pic,font_path="times.ttf",          
             background_color='white',  #设置背景颜色
             max_words=130,           
             max_font_size=150,     
             min_font_size=40,     
             random_state=50, #设置有多少种随机生成状态，即有多少种配色方案
             scale=1) #如设置为1.5，则长和宽都是原来画布的1.5倍
wc.generate_from_frequencies(counts)
plt.figure(figsize=(10,10), dpi=720)
plt.imshow(wc)
plt.axis('off')
plt.show( )


