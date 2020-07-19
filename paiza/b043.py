H, W = list(map(int, input().split(' ')))
h0, w0 = list(map(int, input().split(' ')))
s = [input() for _ in range(H)]
m = []
for _ in range(H):
  m.append([0] * W)
for i in range(len(s)):
  t = s[i]
  j = 0
  for c in t:
    m[i][j] = c
    j += 1
my, mw = [h0, w0]
p = ['↑', '→', '↓', '←']
pi = 0
cc = ''
while True:
  if m[my][mw] == ".":
    if pi < 3:
      pi += 1
    else:
      pi = 0
    cc = '*'
  if m[my][mw] == "*":
    if pi < 0:
      pi = 3
    else:
      pi -= 1
    cc = '.'
  m[my][mw] = cc
  if p[pi] == '↑':
    my, mw = [my - 1, mw]
  if p[pi] == '→':
    my, mw = [my, mw + 1]
  if p[pi] == '↓':
    my, mw = [my + 1, mw]
  if p[pi] == '←':
    my, mw = [my, mw - 1]
  if H - 1 < my or W - 1 < mw or my < 0 or mw < 0:
    break