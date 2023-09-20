class Circle:
    def __init__(self, r):
        self.r = r
    
    def getC(self):
        return 2 * 3.14 * self.r
    
    def getA(self):
        return 3.14 * self.r ** 2
    
    def setR(self, r):
        self.r = r

# 实例化类
c = Circle(1)

# 输出圆的周长和面积
print("圆的周长是：", c.getC())
print("圆的面积是：", c.getA())

# 调用setR方法并重新计算周长和面积
c.setR(7)
print("修改半径后，圆的周长是：", c.getC())
print("修改半径后，圆的面积是：", c.getA())
