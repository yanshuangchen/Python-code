from c_dog import dog
def main():
    #Moki = dog()
    Moki = dog('Moki', '金毛',9)
    print(Moki)
    Moki.bark()      # 执行实例的方法不加参数self
main()
