class Student:
    school='VTS'
   
    def __init__(self,n,r):
        self.name=n
        self.rno=r
        #gloabl
        global add 
        add='Pune'
        #local
        marks=300
      
    def getStudDetails(self):
        print(add)
        print(self.name, self.rno,Student.school)

#1st studnet   
obj=Student('s1',1)  
obj.getStudDetails()

#2nd student 

obj=Student('s2',2)  
obj.getStudDetails()




