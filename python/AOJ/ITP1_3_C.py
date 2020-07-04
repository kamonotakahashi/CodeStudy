L = []
while True:
  x, y = list(map(int, input().split(' ')))
  if x == 0 and y == 0:
    break
  if x < y:
    L.append([x, y])
  else:
    L.append([y, x])
for n in L:
  print(*n)