# 間に合わなかった・・・
N, M, K = list(map(int, input().split(' ')))
r = [int(input()) for _ in range(M)]
s = [0] * N
for i in range(M):
  s[r[i] - 1] = i + 1

for i in range(1, M + 1):
  t = len(s) - 1
  pos = 0
  if i in s:
    pos = s.index(i)
    p = pos - 1
  tt = 0
  while True:
    if p < 0:
      p = t
    if tt < K:
      tt += 1
      p -= 1
      continue
    if p == pos:
      break
    if s[p] == 0:
      s[p] = i
      s[pos] = 0
      break
    p -= 1
for i in range(1, M + 1):
  print(s.index(i))