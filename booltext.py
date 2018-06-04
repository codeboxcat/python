
class MyList:
    def __init__(self,count=0,value=0):
        self.data=[]
        for x in range(count):
            self.data.append(value)
    def __repr__(self):
        return  "MyList("+repr(self.data)+")"

    def __bool__(self):
        print('bool被调用')
        for x in self.data: #遍历对象data属性,
            if x:  #x为真值
                return True
        return False

    def __len__(self):
        return len(self.data)


myl=MyList(10,0)  #0返回到上一条语句，return False 这条

print(myl)  #MyList([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if myl:
    print('MyList为真值')
else:
    print('MyList为假植')

myl=MyList(10,1)
print(myl)
if myl:
    print('MyList为真值')
else:
    print('MyList为假植')
print(len(myl))