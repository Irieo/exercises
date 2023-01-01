input = ['a', 'b', 'c', 'd']

#for i in range(len(input)):
#    print(i, input[i])

[print(i, k) for i, k in enumerate(input)]

print(dict(enumerate(input)))

#type((i, k) for i, k in enumerate(input))