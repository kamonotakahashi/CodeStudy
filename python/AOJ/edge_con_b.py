N = int(input())
a = list(map(int, input().split(' ')))
cnt = 0
for i in range(len(a)):
  if (i+1) % 2 != 0:
    if a[i] % 2 != 0:
      cnt += 1
print(cnt)