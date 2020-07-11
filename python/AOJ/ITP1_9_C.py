n = int(input())
cards = [input() for _ in range(n)]
t = 0
h = 0
for card in cards:
  c = card.split(' ')
  i = 0
  while True:
    l, r = [0, 0]
    if i < len(c[0]):
      l = ord(c[0][i])
    if i < len(c[1]):
      r = ord(c[1][i])
    if l == 0 and r == 0:
      t += 1
      h += 1
      break
    if r < l:
      t += 3
      break
    elif l < r:
      h += 3
      break
    i += 1
print("{0} {1}".format(t, h))