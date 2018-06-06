class Base1:
    def foo1(self):
        print("我是foo1,我为Base1代言......")

class Base2:
    def foo2(self):
        print("我是foo2,我为Base2代言......")

class C(Base1,Base2): #多态继承，C继承了Base1，Base2 两个父类中的方法
    pass

c1=C()
c1.foo1()
c1.foo2()