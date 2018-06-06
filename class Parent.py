# class Parent:
#     def hello(self):
#         print('正在调用父类方法')
#
# class Child(Parent):
#     pass
#
#
# p=Parent()
# p.hello() #正在调用父类方法
#
# c=Child()
# c.hello() #正在调用父类方法
#
# class Child(Parent):
#     def hello(self):
#         print('正在调用子类的方法')
#
# c=Child()
# c.hello() #正在调用子类的方法

import  random as r


class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)

    def move(self):
        self.x -=1
        print('我的位置：',self.x,self.y)


class Goldfish(Fish):# Goldfish继承了Fish这个父类
    pass


class Carp(Fish):#同上，继承Fish父类
    pass


class Salmon(Fish):#同上，继承Fish父类
    pass

class Shark(Fish):
    def __init__(self):
        super().__init__()# 用super函数自动找父类Fish的__init__方法
        self.hungry=True

    def eat(self):
        if self.hungry:
            print('吃吃吃')
            self.hungry=False
        else:
            print('吃饱了')


fish=Fish()#实例化一个创世鱼
fish.move()#初始化创世鱼的位置
goldfish=Goldfish()#实例化一个goldfish
goldfish.move() #goldfish继承了Fish父类中的move方法
shark=Shark()#实例化一个shark
shark.eat()# 调用子类的方法eat：吃吃吃
shark.eat()# 调用子类的方法eat：吃饱了
shark.move()#子类重写了父类Fish中__init__这个方法，父类Fish中的__init__方法会被覆盖，因此会报错。
#修改上一条语句方法:使用super()函数:super.__init__()
















