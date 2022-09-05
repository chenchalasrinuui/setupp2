#assign to one variable & call
'''
f=lambda:print('called')
f()

'''
# self invoking 

'''
(lambda:print('called'))()

'''
# pass as an argument to one fuction & call
'''
def f1(a):
    a()

f1(lambda:print('called'))

'''

# call lamda fuction with arguments

'''
def f1(a):
    a('Sachin','Mumbai')

f1(lambda name,loc:print(name,loc))
'''


def f1(a):
    a('Sachin','Mumbai')

def getInfo(name,loc):
    print('My name is ',name)
    print('location is ',loc)

f1(lambda name,loc:getInfo(name,loc))


