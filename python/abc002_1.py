import sys
put = input().split(" ")
X = int(put[0])
Y = int(put[1])
if not (0 <= X and Y <= 10**9) or X == Y:
    sys.exit()
S = X if X > Y else Y
print(S)
