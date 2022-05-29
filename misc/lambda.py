# lambda function 1

def add(x,y):
    return x+y

x = 2
y = 3

add(x,y)

f1 = lambda x,y: x+y
f1(2,5)

# lambda function 2 

def mx(x,y):
    if x>y:
        return x
    else:
        return y

mx(x,y)

f2 = lambda x,y: x if x>y else y

f2(2,10.1)
