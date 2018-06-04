class A:
    pass

    def __init__(self):
        self.data=0

    def __call__(self, *args,**kwargs):# 只有call这个重载方法，后面参数可以是多个！call方法多用在计数。
        '''函数调用方法重载'''

        print('args:',args,'kwargs:',kwargs)
        print('__call__方法被调用')
        s=(sum(args)) #300
        self.data+=s
        return s




a=A() #创建对象a，且能被调用了。a得到的值就是call方法return的100
print(a(100,200))  #把这种能被调用的对象，可成为函数对象.
r=a(300,400)
print(r)
print('以前所有的数之和为:',a.data)# 所有数相加之和，self.data+=s