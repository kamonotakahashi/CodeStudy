n = int(input())
l = []
for i in range(4):
  l.append([])
  for x in range(3):
    l[i].append([0] * 10)
for nn in range(n):
  b, f, r, v = list(map(int, input().split(' ')))
  l[b - 1][f - 1][r - 1] += v
i = 0
for n in l:
  for nn in n:
    for nnn in nn:
      print(' {0}'.format(nnn), end='')
    print('', sep='\n')
  i += 1
  if i == len(l):
    break
  print('####################')