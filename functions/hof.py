def f1(a,b):
    a('Sachin')
    b('Dhoni')
    def f2(name):
        return name
    return f2('Kohli')


def f3(name):
    print(name)

def f4(name):
    print(name)

x=f1(f3,f4)
print(x)







