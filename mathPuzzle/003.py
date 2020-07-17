N = 100

c = [0] * N
pos = 2
cnt = 0
while True:
  cnt += pos
  if cnt < len(c):
   c[cnt - 1] = 1 if 0 == c[cnt - 1] else 0
  else:
    if len(c) - 1 <= pos:
      break
    cnt = 0
    pos += 1
for i in range(len(c)):
  if c[i] == 0:
    print(i + 1)