def b(value, n):
  tmp = int(value)
  result = ''
  while tmp >= n:
      result = str(tmp%n) + result
      tmp = int(tmp / n)
  result = str(tmp%n) + result
  return result
N = 0
while True:
  N += 1
  if N < 10:
    continue
  d = str(b(N, 2))
  o = str(b(N, 8))
  c = str(N)
  if d == d[::-1] and o == o[::-1] and c == c[::-1]:
    break
print(N)