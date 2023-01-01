import timeit

#print(timeit.timeit('1+3', number = 10000))

#print('a')

input_list = range(100)

def div_five(num):
    return True if num % 5 == 0 else False

lst = [i for i in input_list if div_five(i)]
lst = (i for i in input_list if div_five(i))

print(timeit.timeit('''
input_list = range(100)

def div_five(num):
    return True if num % 5 == 0 else False

lst = [i for i in input_list if div_five(i)]''', number = 100000))
