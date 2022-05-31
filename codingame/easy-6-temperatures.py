input()  # skip
lst = input() or '0'

temps = [int(s) for s in lst.split()]

if len(temps) == 0:
    print(0)
else:
    r = list(min((abs(x), x) for x in temps))[:]
    print(r[0] if (r[1] and r[0]) in temps else r[1])

#alternative:
#temps.sort(key = lambda x: (abs(x),-x))
#print(temps[0])
