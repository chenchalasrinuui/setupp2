class A:
    def f1(self):
        print('f1 called')
    def f2():
        print('f2 called')

obj=A()
obj.f1()  # obj.f1(obj)
A.f2() # A.f2()