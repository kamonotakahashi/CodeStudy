# コードの最適化が必要
import sys
import re
try:
  t = input().split(' ')
  N = int(t[0])
  M = int(t[1])
  K = int(t[2])
  S = 0
  A = [int(n) for n in input().split(' ')]
  B = [int(n) for n in input().split(' ')]
  if not 1 <= N <= 200000 or not 1 <= M <= 200000 or not 1 <= K <= (10**9):
    sys.exit()

  C = N if M < N else M
  BC = 0
  for l in range(C):
    if l+1 <= N:
      if not 1 <= A[l] <= (10**9):
        sys.exit()
      S += A[l]
      BC += 1
      if not S <= K:
        BC -= 1
        break
    if l+1 <= M:
      if not 1 <= B[l] <= (10**9):
        sys.exit()
      S += B[l]
      BC += 1
      if not S <= K:
        BC -= 1
        break
  print(BC)
except Exception as err:
  sys.exit()