import sys
import math
io = input().split(' ')
N = int(io[0])
M = int(io[1])
if not (1 <= N <= 1000) or not (1 <= M <= 100):
    sys.exit()
A = input().split(' ')
if not len(A) <= N:
    sys.exit()
Q = int(input())
if not 1 <= Q <= 1000:
    sys.exit()
value = 0
for l in range(0, Q):
    io = input().split(' ')
    s = int(io[0])
    e = int(io[1])
    if not 1 <= s <= e <= N:
        sys.exit()
    c = A[s - 1:e]
    sum = 0
    value = 0
    p = s - 1
    for cc in c:
        sum += int(cc)
    value = math.floor(sum/len(c))
    #print(value)
    add = 0
    if value < M:
        add = abs(M - value)
        for i in range(0, len(c)):
            if p >= e:
                break
            A[p] = int(A[p]) + add
            p = p + 1
tt = ''
for aa in A:
    tt += str(aa) + " "
print(tt.strip())
