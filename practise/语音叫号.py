'''import pyttsx3

# 创建TTS引擎
engine = pyttsx3.init()

# 设置要朗读的文本
text = "请78号同学取餐"

# 将文本传递给引擎
engine.say(text)

# 等待引擎完成语音合成
engine.runAndWait()'''
import pyttsx3

# 初始化语音引擎
engine = pyttsx3.init()

# 获取用户输入的数字
num = input("请输入一个数字: ")

# 将数字转换为语音输出 


engine.say(f"烤盘饭，请{num}号顾客取餐")
engine.runAndWait()
'''import pyttsx3

# 初始化 pyttsx3 引擎
engine = pyttsx3.init()

# 设置语音速度
engine.setProperty('rate', 150)   # 值的范围为[0, 500]

# 设置语音音量
engine.setProperty('volume', 0.8) # 值的范围为[0, 1]

# 设置语音的声音类型
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0为男性声音，1为女性声音

# 将文本转换为语音输出
engine.say('Hello, world!')

# 等待语音播放完毕
engine.runAndWait()'''