n = int(input())
min_dif = float('inf')

powers = sorted([int(input()) for _ in range(n)])

for i in range(0, n-1):
    dif =  powers[i + 1] - powers[i]
    if dif < min_dif: min_dif = dif

print (min_dif)
