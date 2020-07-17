import sys
#なぜかランタイムエラー　４０点
io = input().split(' ')
M = int(io[0])
N = int(io[1])
K = int(io[2])
if not (1<=M<=100) or not (1<=N<=100) or not (1<=K<=100):
    sys.exit()
ai = []
sq = [ 0 for i in range(K)]
for i in range(0, K):
    io = input()
    if not 1<=int(io)<=M:
        sys.exit()
    ai.append(int(io))

b = 0
e = 0
buf = 0
amari = N
for l in ai:
    b = l - 1
    if 0 < amari:
        if (b == e):
            sq[b] = sq[b] + 1
        else:
            sq[b] = sq[b] + 1
            buf = sq[b]
            sq[b] = sq[e]
            sq[e] = buf
        amari = amari - 1
    else:
        buf = sq[b]
        sq[b] = sq[e]
        sq[e] = buf
    e = b
max = 0
for n in sq:
    if max < n:
        max = n
t = []
for c in range(0, len(sq)):
    if max == sq[c]:
        print(c + 1)
