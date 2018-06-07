class Human:
    def __int__(self,name,age):
        self.name=name
        self.age=age

    def infos(self):
        print('我叫:',self.name,'我今年:',self.age,'岁')

    def say(self,what):
        print('说:',what)

    def run(self,speed):
        print('正在以',speed,'m/s速度奔跑!')

h1=Human()
h1.say('天气真好')
h1.run(5)

class Student(Human):# 这个类描述了Human类的一切方法，同时又添加了其他的study这个函数。
    '''这个类继承了Human类的所有功能，并进行了扩展。student类叫子类，Human是
        Student的父类。
    '''
    # def say(self,what):
    #     print('说:',what)
    #
    # def run(self,speed):
    #     print('正在以',speed,'m/s速度奔跑!')

    def study(self,progam):
        print('正在学习:',progam)


s1=Student()
s1.say('午餐吃什么？')
s1.run(6)
s1.study('python3')













