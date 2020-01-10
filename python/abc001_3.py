import sys

d = input().split(" ")
deg = int(d[0])
dis = int(d[1])

if not (0 <= deg < 3600) or not (0 <= dis < 12000):
    sys.exit()
