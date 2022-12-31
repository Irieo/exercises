import random 

l = [random.randint(1,30) for i in range(10)]
#print(l)

def div_five(num):    
    return True if num % 3 == 0 else False


lst = [i for i in l if div_five(i)]

gen = (i for i in l if div_five(i))

#[print(i) for i in gen]

#############3

#[[print(k,kk) for kk in ['a','b', 'c']] for k in range(3)]

[[[k,kk] for kk in ['a','b', 'c']] for k in range(3)]

long = (((k,kk) for kk in range(10000)) for k in range(100000))

for k in long:
    for kk in k:
        print(kk)