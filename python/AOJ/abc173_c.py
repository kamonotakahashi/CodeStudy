H, W, K=map(int,input().split())
F = [input() for _ in range(H)]
ans = 0
for i in range(2**H):
  for j in range(2**W):
    cnt = 0
    for ii in range(H):
      for jj in range(W):
        if (i>>ii)%2==0 or (j>>jj)%2==0 or F[ii][jj]==".":
          continue
        cnt+=1
    if cnt==K:
      ans+=1
print(ans)