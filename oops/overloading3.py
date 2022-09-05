class Arth:
    def sum(self,n1=None,n2=None,n3=None):
        if(n1!=None and n2 != None and n3 !=None):
            print(n1+n2+n3)
        elif(n1!=None and n2!=None):
            print(n1+n2)
        else:
            print(n1)
        

obj=Arth()
obj.sum(1,2,3)
obj.sum(1,2)
obj.sum(100)