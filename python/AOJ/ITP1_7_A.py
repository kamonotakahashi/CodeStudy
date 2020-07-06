ans = []
while True:
  m, f, r = list(map(int, input().split(' ')))
  if m == -1 and f == -1 and r == -1:
    break
  if  m == -1 or f == -1:
    ans.append('F')
  elif 80 <= m+f:
    ans.append('A')
  elif 65 <= m+f < 80:
    ans.append('B')
  elif 50 <= m+f < 65:
    ans.append('C')
  elif 30 <= m+f < 50:
    if 50 <= r:
      ans.append('C')
    else:
      ans.append('D')
  else:
    ans.append('F')
for n in ans:
  print(n)