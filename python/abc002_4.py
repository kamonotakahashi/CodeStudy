import sys
in = input().split(' ')
N = in[0]
M = in[1]
if not (1 <= int(N) <= 12) or not (0 <= int(M) <= floor((N*N-N)/2)):
    sys.exit()
print("a")
