r, c = list(map(int, input().split(' ')))
l = []
for i in range(r):
    l.append(list(map(int, input().split(' '))))
yl = []
xl = []
for y in range(r):
    xl.append(0)
    for x in range(c):
        xl[y] += l[y][x]
    l[y].append(xl[y])
t = [0] * len(l[0])
for y in range(r):
    for x in range(len(t)):
        t[x] += l[y][x]
l.append(t)
for a in l:
    print(*a)