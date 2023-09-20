class dog:
    """狗类的创建例子"""
    def __init__(self,name="bobo", kind="猎犬",month_age=20):
        self.name = name
        self.month_age=month_age
        self.kind = kind
    def __str__(self):
        return '<狗名: %s(%s，%d个月)>' % (self.name, self.kind, self.month_age)	
    def bark(self):   # 类方法必须包含参数self
        print('汪汪')
