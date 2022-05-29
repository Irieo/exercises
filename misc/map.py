# map function

lst1 = [1,2,3,4]

# standard function
def square(lst1):
    lst2 = []
    for num in lst1:
        lst2.append(num**2)
    return lst2

square(lst1)

# map with lambda
list(map(lambda x: x**2, lst1))

# map w/o lambda 
def sq(x):
    return x**2

list(map(sq, lst1))

# via list comprehension
[x**2 for x in lst1]