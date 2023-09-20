# 基本用法
name = 'Alice'
age = 30
print('My name is {}, and I am {} years old.'.format(name, age))

# 使用参数索引
print('{1} is {0} years old.'.format(age, name))

# 使用参数名称
print('My name is {name}, and I am {age} years old.'.format(name=name, age=age))

# 使用属性和方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '{} ({})'.format(self.name, self.age)
    
person = Person('Bob', 25)
print('My friend is {}.'.format(person))

# 格式化数字
pi = 3.141592653589793
print('The value of pi is {:.2f}.'.format(pi))  # 保留两位小数

# 格式化日期
import datetime
now = datetime.datetime.now()
print('Today is {:%Y-%m-%d %H:%M:%S}.'.format(now))  # 输出格式为：年-月-日 小时:分钟:秒
