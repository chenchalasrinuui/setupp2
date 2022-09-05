
class B:
    def __init__(self):
        print('B con')
        self.n2=20

class A(B):
    n1=10
    def __init__(self):
        #B.__init__(self)
        super().__init__()
        print('A con')
    def sum(self):
        print(A.n1+self.n2)

o=A()
o.sum()