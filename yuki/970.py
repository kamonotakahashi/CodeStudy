import sys
import random
import math

N = int(input())

if not (2 <= N <= 10 ** 5):
    sys.exit()

Y = input().split(" ")

if not N == len(Y):
    sys.exit()
cc = []
for l in range(0, len(Y)):
    c = int(Y[l])
    if not (-1000 <= c <= 1000):
        sys.exit()
    cc.append(c * 2)

dd = [0] * N
sum = 0
for c in range(0, len(cc)):
    while(1):
        for l in range(0, len(cc)):
            if not l == c:
                dd[l] = random.randrange(int(cc[c]))
                sum = sum + dd[l]
        print("cc={0},sum={1}".format(cc[c],sum))
        if cc[c] == sum:
            break
        sum = 0
