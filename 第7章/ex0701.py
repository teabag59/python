#ex0701.py
class Dog:
    num = 0              #类属性
    def __init__(self,id=0,color="yellow"):#构造方法
        self.id=id
        self.color=color
        
    def enjoy(self):     #成员方法
        print("wangwang")

dog1 =Dog()
dog1.enjoy()

dog2 =Dog()
