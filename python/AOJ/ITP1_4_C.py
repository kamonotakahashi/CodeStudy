l = []
while True:
  a, op, b = list(map(str, input().split(' ')))
  a, b = [int(a), int(b)]
  ans = 0
  if op == '?':
    break
  if op == '+':
    ans = a + b
  if op == '-':
    ans = a - b
  if op == '/':
    ans = int(a / b)
  if op == '*':
    ans = a * b
  l.append(ans)
for n in l:
  print(n)