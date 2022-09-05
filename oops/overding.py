class Parent:
    def property(self):
        print('1cr')
class Children(Parent):
    def property(self):
        print('100cr') 

obj=Children()
obj.property()