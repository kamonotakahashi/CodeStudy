N = int(input())
m = [input() for _ in range(N)]
chk = []
for i in range(len(m)):
  m[i] = list(map(int, m[i].split(' ')))
for i in range(N):
  col = 0
  row = 0
  for j in range(N):
    col += m[i][j]
    row += m[j][i]
  chk.append([col, row])
st = []
ct = -1
for c, r in chk:
  if c == r:
    ct = c
tt = []
for c, r in chk:
  rr = 0
  cc = 0
  if r != ct:
    rr = ct - r
  if c != ct:
    cc = ct - c - rr
  if 0 != cc:
    tt.append(cc)
  if 0 != rr:
    tt.append(rr)
c = [x for x in set(tt) if tt.count(x) >= 1]
for l in range(2):
  cnt = 0
  mt = m
  for i in range(N):
    col = 0
    row = 0
    for j in range(N):
      if mt[i][j] == 0:
        mt[i][j] = c[cnt]
        cnt += 1
  if col == st and row ==st:
    break
  c.reverse()
for a in mt:
  print(*a)