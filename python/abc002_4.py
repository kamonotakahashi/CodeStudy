import sys
import math
io = input().split(' ')
N = int(io[0])
M = int(io[1])
if not (1 <= N <= 12) or not (0 <= M <= math.floor((N*N-N)/2)):
    sys.exit()
for l in range(0, M):
    print(l)
