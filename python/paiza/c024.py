n = int(input())
s = [input() for _ in range(n)]
a = [0] * 2
for l in s:
  t = l.split(' ')
  if t[0] == 'SET':
    a[int(t[1]) - 1] = int(t[2])
  if t[0] == 'ADD':
    a[1] = a[0] + int(t[1])
  if t[0] == 'SUB':
    a[1] = a[0] - int(t[1])
print(a[0], a[1])