class A:
    n1=10

class B(A):
    n2=20

class C(B):
    n3=30
    
    def sum(self):
        print(self.n1+self.n2+self.n3)


obj=C()
obj.sum()