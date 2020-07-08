X = int(input())
f00 = X//500
f = int(X - (f00/2 * 1000)) // 5
print(f00 * 1000 + f * 5)