a = []
while True:
  H, W = list(map(int, input().split(' ')))
  if H == 0 and W == 0:
    break
  a.append([H, W])
for l in a:
  for h in range(l[0]):
    for w in range(l[1]):
      if (w == 0 or w == l[1] - 1) or (h == 0 or h == l[0] - 1):
        print('#', end='')
      else:
        print('.', end='')
    print('', sep="\n")
  print('', sep="\n")