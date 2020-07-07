import re
a = [chr(i) for i in range(ord('a'), ord('z')+1)]
l = [0] * len(a)
while True:
  try:
    s = str(input())
  except:
    break
  for c in s:
    p = 0
    if re.match(r'^[a-zA-Z]$', c):
      p = a.index(c.lower())
      l[p] += 1

for i in range(len(a)):
  print("{0} : {1}".format(a[i], l[i]))