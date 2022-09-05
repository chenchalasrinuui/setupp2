class Student:
    def __init__(self,n,r):
        self.name=n
        self.rno=r
        
    def getStudDetails(self):
        print(self.name, Student.rno)

#1st studnet   
obj=Student('s1',1) 
obj.getStudDetails()

#2nd student 

obj=Student('s2',2)  
obj.getStudDetails()




