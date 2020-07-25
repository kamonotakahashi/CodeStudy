A, B, C = list(map(int, input().split(' ')))
K = int(input())
cnt = 0
flg = 0
while cnt < K:

  if B <= A:
    B *= 2
  elif C <= B:
    C *= 2
  cnt += 1

  if A < B < C:
    flg = 1
    break

if flg == 1:
  print("Yes")
else:
  print("No")