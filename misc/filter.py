# standard function

lst = [1,2,4,6,7,3,2,5,5]

def over_two(n):
    r = [x for x in n if x>2]
    return r

over_two(lst)

# filter(condition, iterable)
list(filter(lambda x: x>2, lst))

# but also as list comprehension
[x for x in lst if x>2]
