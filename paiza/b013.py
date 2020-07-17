#encoding: utf-8
import sys
import datetime

ldate = datetime.datetime(2020, 1, 19, 9, 0, 0)
io = input().split(' ')
a = int(io[0])
b = int(io[1])
c = int(io[2])
time = []
srctime = []
s_seconds = a * 60
t_seconds = b * 60 + c * 60

if not (1 <= a <= 30) or not (1 <= b <= 30) or not (1 <= c <= 30) :
    sys.exit()
N = int(input())
if not 1 <= N <= 180:
    sys.exit()
for l in range(0, N):
    t = input().split(' ')
    h = int(t[0])
    m = int(t[1])
    if not (6 <= h <= 8) or not (0 <= m <= 59):
        sys.exit()
    time.append( datetime.datetime(2020, 1, 19, h, m, 0) )
max = 0
hit = 0
for i in range(0, len(time)):
    arrival = time[i] + datetime.timedelta(seconds=t_seconds)
    if arrival < ldate:
        if max == 0:
            max = arrival
            hit = i
        else:
            if max < arrival:
                max = arrival
                hit = i
tt = time[hit] - datetime.timedelta(seconds=s_seconds)
print(tt.strftime("%H:%M"))
