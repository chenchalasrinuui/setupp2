marks=[500, 333,222,343,565,555]

def f1(val):
    print(val)
    return val>500

output=filter(f1,marks)
print(list(output)) 
