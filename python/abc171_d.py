# ダメでした・・・・
N = int(input())
A = list(map(int, input().split(' ')))
Q = int(input())
def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

SS = []
for ll in range(0, Q):
  c = list(map(int, input().split(' ')))
  t = my_index(A, c[0], -1)
  while t != -1:
    A[t] = c[1]
    t = my_index(A, c[0], -1)
  FS = sum(A)
  SS.append(FS)
for s in SS:
  print(s)