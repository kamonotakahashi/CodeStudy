n = int(input())
i = 1
l = []
while i <= n:
  x = i
  if x % 3 == 0:
    l.append(i)
  else:
    while x:
      if int(x) % 10 == 3:
        l.append(i)
        break
      x /= 10
  i += 1
for n in l:
  print(" {0}".format(n), end='')
print('', sep='\n')