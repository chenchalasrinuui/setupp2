class A:
   
    @classmethod
    def f1(cls):
        print(cls)
        print('f1 called')
    @classmethod
    def f2(cls):
        print(cls)
        print('f1 called')

obj=A()
obj.f1() #obj.f1(A)
A.f2() #A.f2(A)
