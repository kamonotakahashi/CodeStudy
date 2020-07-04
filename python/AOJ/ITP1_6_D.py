n, m = list(map(int, input().split(' ')))
A = []
b = []
for i in range(n):
  A.append(list(map(int, input().split(' '))))
for i in range(m):
  b.append(int(input()))
for i in range(n):
  s = 0
  for x in range(m):
    s += A[i][x] * b[x]
  print(s)