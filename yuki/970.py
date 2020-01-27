import sys

N = int(input())

if not (2 <= N <= 10 ** 5):
    sys.exit()

Y = input().split(" ")

if not N == len(Y):
    sys.exit()
##
for l in range(0, len(Y)):
    c = int(Y[l])
    s = 1
    e = c*2 - 1
    if not (-1000 <= c <= 1000):
        sys.exit()
    while 1:
        if(s > e):
            break
        print("{0},{1}".format(s,e))
        s = s + 1
        e = e - 1
