l =[]
while True:
    n, x = list(map(int, input().split(' ')))
    if n == 0 and x == 0:
        break
    l.append([n, x])
for a in l:
    aa = [ i for i in range(1, a[0] + 1)]
    s = 0
    for i in range(0, len(aa) + 1):
        for j in range(i + 1, len(aa) + 1):
            for k in range(j + 1, len(aa)):
                t = aa[i] + aa[j] + aa[k]
                if t == a[1]:
                    s += 1
    print(s)