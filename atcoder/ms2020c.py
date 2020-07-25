# TLE
N, K = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
L = []
s = 0
while True:
  if len(A) < s + K:
    break
  su = 1
  for n in A[s:s + K]:
    su *= n
  L.append(su)
  if 1 < len(L):
    if L[s - 1] < L[s]:
      print('Yes')
    else:
      print('No')
  s += 1