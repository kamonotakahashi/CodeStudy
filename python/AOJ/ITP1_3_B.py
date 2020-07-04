l = []
while True:
  io = int(input())
  if io == 0:
    break
  l.append(io)
i = 1
for n in l:
  print("Case {0}: {1}".format(i, n))
  i += 1