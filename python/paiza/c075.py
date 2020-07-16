N, M = list(map(int, input().split(' ')))
c = [int(input()) for _ in range(M)]
p = 0
for l in c:
  if p >= l:
    p -= l
  else:
    N -= l
    p += int(l * 0.1)
  print(N, p)