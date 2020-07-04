a, b = list(map(int, input().split(' ')))
d = int(a / b)
r = a % b
f = a / b
print("{0} {1} {2:.8f}".format(d, r, f))