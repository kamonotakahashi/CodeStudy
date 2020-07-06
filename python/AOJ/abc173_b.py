N = int(input())
A = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for l in range(N):
  S = str(input())
  A[S] += 1
for n in A:
  print("{0} x {1}".format(n, A[n]))