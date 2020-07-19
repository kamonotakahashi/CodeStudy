Q = int(input())
N = [int(input()) for _ in range(Q)]
a = ['perfect', 'nearly', 'neither']
cnt = 0
while True:
  if len(N) - 1 < cnt:
    break
  s = 0
  for i in range(1, N[cnt] + 1):
    if N[cnt] % i == 0 and i < N[cnt] - 1:
      s += i
  print(a[0] if s == N[cnt] else a[1] if 1 == abs(s - N[cnt]) else a[2])
  cnt += 1