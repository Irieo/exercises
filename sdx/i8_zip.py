a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
c = ['a', 'b', 'c', 'k']


for x,y,z in zip(a,b,c):
    print(y,z)

print(type(zip(a,b,c)))

for i in zip(a,b,c):
    print(i)

print(list(zip(a,b,c)))

print(dict(zip(a,c)))

# Dont use same variables for iteration as your inputs. 
# It won't be a problem in list comprehension, but WILL overwrite input in a standard `for` loop

[print(a,b) for a,b in zip(a,b)]

print(b)

for a,b in zip(a,b):
    print(a,b)

print(b) #b is overwritten