
from functools import reduce

marks=[99, 88,33,86,77,88]

output=reduce(lambda initial,val:initial+val,marks)
print(output)