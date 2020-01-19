#encoding: utf-8
import sys
io = input().split(' ')
H = int(io[0])
W = int(io[1])
if not (2 <= H <= 100) or not (2 <= W <= 100):
    sys.exit()
line1 = input().split(' ')
line2 = input().split(' ')
line = [[0 for i in range(W)] for j in range(H)]
line[0][0] = int(line1[0])
line[0][1] = int(line1[1])
line[1][0] = int(line2[0])
line[1][1] = int(line2[1])
inc = 0
for y in range(0, W):
    for x in range(0, H):
        if 0 < x:
            inc = abs(line[y][x] + line[y][x])
        if not 1 < x and not 1 < y:
            line[y][x] = line[y][x - 1]
