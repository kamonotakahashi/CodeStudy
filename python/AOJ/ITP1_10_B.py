import math
a, b, C = list(map(int, input().split(' ')))
c = math.sqrt(a**2 + b**2)
PI = math.acos(-1)
rad = C * PI / 180
h = b * math.sin(rad)
S = 1/2*a*h
L = a + b + math.sqrt(a**2 + b**2 - 2*a*b * math.cos(rad))
print("{0:.8f}".format(S))
print("{0:.8f}".format(L))
print("{0:.8f}".format(h))