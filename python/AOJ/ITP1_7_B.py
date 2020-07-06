l = []
while True:
  n, x = list(map(int, input().split(' ')))
  if n == 0 or x == 0:
    break
  l.append([n, x])
for a in l:
  aa = [ i for i in range(1, a[0] + 1)]
  for i in range(0, len(aa)):
    print(aa[i], end="")
    for j in range(i + 1, len(aa) - i):
      print(aa[j], end="")
      for k in range(i + j + 1, len(aa) - i - j):
        print(aa[k], end="")
    print('', sep="\n")