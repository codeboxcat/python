class A(object):
    def hello(self):
        print("A类的hello(self)")


class B(A):
    def hello(self):
        print("B类的Hello(self)")

    def super_hello(self):#此方法调用基类的hello方法

        super().hello()#super(B,self).hello() 打印结果:A类的hello(self)


b=B()
b.hello()  #B类的Hello(self)

#用 super函数调用基类的方法:
super(B,b).hello()#A类的hello(self)
B.__base__.hello(b)#作用等同于上一条语句

b.super_hello()#A类的hello(self)