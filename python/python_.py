N = int(input())
ans = 0
for j in range(1, N+1):
    for i in range(1, N+1):
        if i % j == 0:
            ans += i
print(ans)