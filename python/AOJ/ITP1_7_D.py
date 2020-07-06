n, m, l = list(map(int, input().split(' ')))
A = []
B = []
for i in range(n):
    A.append(list(map(int, input().split(' '))))
for i in range(m):
    B.append(list(map(int, input().split(' '))))
C = []
for i in range(n):
    C.append([0] * l)
for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
for a in C:
    print(*a)