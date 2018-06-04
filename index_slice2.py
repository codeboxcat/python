
class MyList:
    def __init__(self,count=0,value=0):
        self.data=[]
        for x in range(count):
            self.data.append(value)

    def __repr__(self):
        return "MyList("+repr(self.data)+")"

    def setValueAt(self,index,value):
        self.data[index]=value

    def __setitem__(self, index, value):
        if isinstance(index,int):
            return self.data[index]
        elif isinstance(index,slice):
            print("开始值:",index.start)
            print('结束值:',index.stop)
            print('步长:',index.step)
            L = self.data[index]  # 把列表通过切片index 给到L，创建一个空列表
            ml = MyList()
            for x in L:
                ml.data.append(x)  # ml创建的空列表把x遍历后添加到这个空列表中
            return ml

        # self.data[index]=value

    def __getitem__(self, index):
        print('__getitem__被调用,index的值为:',index)
        if isinstance(index,int):
            return self.data[index]
        elif isinstance(index,slice):
            print("开始值:",index.start)
            print('结束值:',index.stop)
            print('步长:',index.step)
            L=self.data[index]# 把列表通过切片index 给到L，创建一个空列表
            ml=MyList()
            for x in L:
                ml.data.append(x) #ml创建的空列表把x遍历后添加到这个空列表中
            return ml

        # return self.data[index]

    def __delitem__(self, index):
        if index >=len(self.data):
            raise IndexError('%d在不允许范内'%index)
        if index<-len(self.data):
            raise IndexError('%d在不允许范内' % index)
        del self.data[index]



myl=MyList(5,1) #MyList(1,2,3,4,5])
myl[1]=2
myl[2]=3
myl[3]=4
myl[4]=5
print(myl)
print(myl[1])#2
print(myl[1:5:2])#会生成一个slice对象，等同于print(myl[slice(1,5,2)])

#将index_slice2.py 修改方法:__setitem__(self,index,value),如果myl[::10],print(myl)

myl[::10]
print(myl)