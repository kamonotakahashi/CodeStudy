l = []
while True:
  x = int(input())
  if x == 0:
    break
  t = 0
  for n in str(x):
    t += int(n)
  l.append(t)
for s in l:
  print(s)