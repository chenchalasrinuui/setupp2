class A:
    def f2(self):
        print('f2 from A')

class B:
    def f2(self):
        print('f2 from B')

class C(A,B):
    def f1(self):
        print('f1 from C')
    def f3(self):
        print('f3 from C')

obj=C()
obj.f1()
obj.f2()