N, M = list(map(int, input().split(' ')))
a = [input() for _ in range(N)]
cnt = 1
for c in a:
  a, b = list(map(int, c.split(' ')))
  if abs( a - 5*b) >= M:
    print(cnt)
  cnt += 1