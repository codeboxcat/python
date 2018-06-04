#定义一个表示素数的类：
# def isprime(x):  #放在全局来使用
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

class Primes:
    def __init__(self,end):
        '''end用于表示素数的终止点，素数的起始点是2(包含2)'''
        self.end=end

        @staticmethod #静态方法,需要借助一个对象或者类才能调用。
        def isprime(x):
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True

    def __contains__(self, element):
        # def isprime(x): #isprime()定义在类内，只能在类内使用。如果定义在外部，可以在全局调用。
        #
        #     for i in range(2,x):
        #         if x%i==0:
        #             return False
        #     return True
        if element<2:
            return False
        if element>=self.end:
            return False
        return self.isprime(element)




p1=Primes(100)
if 53 in p1:
    print('53是素数')
else:
    print('53不是素数')

print(Primes.isprime(53))
