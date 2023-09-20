import chardet

with open(r"C:\Users\86138\Desktop\相关性个数.xlsx", 'rb') as f:
    result = chardet.detect(f.read())

print(result)