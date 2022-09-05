class A:
    n1=10

class B:
    n2=20
    n1=100

class C(A,B):
    n3=30
    
    def sum(self):
        print(self.n1+self.n2+self.n3)


obj=C()
obj.sum()