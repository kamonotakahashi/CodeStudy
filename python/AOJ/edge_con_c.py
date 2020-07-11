N = int(input())
ans = [ 0 for _ in range(10500)]
for i in range(1, 105):
  for j in range(1, 105):
    for k in range(1, 105):
      v = i**2 + j**2 + k**2 + i*j + j*k + k*i
      if v < 10500:
        ans[v] += 1
for i in range(N):
  print(ans[i + 1])