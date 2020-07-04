n = int(input())
A = {'S':[],'H':[],'C':[],'D':[]}
M = {'S':[],'H':[],'C':[],'D':[]}
for i in range(n):
  a, b = list(map(str, input().split(' ')))
  A[a].append(int(b))
for l in A:
  cnt = 0
  for ll in range(1, 13 + 1):
    if not ll in A[l]:
      M[l].append(ll)
  M[l].sort()
  if 0 < len(M[l]):
    for o in M[l]:
      print('{0} {1}'.format(l, o))