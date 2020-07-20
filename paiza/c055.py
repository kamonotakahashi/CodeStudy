N = int(input())
G = input()
S = [input() for _ in range(N)]
ans = []
for l in S:
  if 0 <= l.find(G):
    ans.append(l)
if 0 < len(ans):
  for l in ans:
    print(l)
else:
  print('None')