class A:
   
    @staticmethod
    def f1():
        print('f1 called')

    @staticmethod
    def f2():
        print('f2 called')
        
   


obj=A()
obj.f1() # obj.f1()
A.f2()