
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
        self.data[index]=value

    def __getitem__(self, index):
        print('__getitem__被调用,index的值为:',index)

        return self.data[index]

    def __delitem__(self, index):
        if index >=len(self.data):
            raise IndexError('%d在不允许范内'%index)
        if index<-len(self.data):
            raise IndexError('%d在不允许范内' % index)
        del self.data[index]
        #以下示意不允许使用del 进行索引操作
        # print('__delitem__被调用',index)
        # print('__delitem__啥也没做！')
        # raise IndexError





myl=MyList(5,1) #MyList([1,1,1,1,1])
myl[1]=2
print(myl[0])#1
print(myl) #MyList([1, 2, 1, 1, 1])
# myl.setValueAt(1,2)#MyList([1,2,1,1,1])
del myl[3]
print(myl)#MyList([1, 2, 1, 1])

