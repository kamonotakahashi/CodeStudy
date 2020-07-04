a = []
while True:
  H, W = list(map(int, input().split(' ')))
  if H == 0 and W == 0:
    break
  a.append([H, W])
for l in a:
  for h in range(l[0]):
    for w in range(l[1]):
      print('#', end='')
    print('', sep="\n")
  print('', sep="\n")