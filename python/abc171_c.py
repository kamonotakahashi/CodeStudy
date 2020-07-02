N = int(input())
T = N
KISU = 26
Y = []
A = [chr(ord('a') + i) for i in range(26)]
ans = ''
S1 = 0
S1 = 25 if S1 == 0 else S1
while True:
  if T == 0:
    break
  S1 = (T % KISU)
  S1 = 26 if S1 == 0 else S1
  Y.append(S1)
  if S1 == 26:
    T -= 1
  T = T//KISU
for n in Y[::-1]:
  ans += A[n - 1]
print(ans)