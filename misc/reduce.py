# standard function

lst = [4,3,2,1]

def mult(n):
    prod = lst[0]
    for i in range(1,len(lst)):
        prod *= lst[i]
    return prod

mult(lst)


# reduce(function, iterable)
from functools import reduce

reduce(lambda x,y: x*y, lst)