a, b, c = list(map(int, input().split(' ')))
l = [n for n in range(a, b + 1)]
ans = 0
for n in l:
  if c % n == 0:
    ans += 1
print(ans)