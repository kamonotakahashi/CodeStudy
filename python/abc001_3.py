import sys
import math

d = input().split(" ")
deg = round(int(d[0]) / 10, 1)
dis = int(d[1])

if not (0 <= deg < 360) or not (0 <= dis < 12000):
    sys.exit()
#
hougaku = [
    [11.25,"NNE"],
    [33.75,"NE"],
    [56.25,"ENE"],
    [78.75,"E"],
    [101.25,"ESE"],
    [123.75,"SE"],
    [146.25,"SSE"],
    [168.75,"S"],
    [168.75,"S"],
    [191.25,"SSW"],
    [213.75,"SW"],
    [236.25,"WSW"],
    [258.75,"W"],
    [281.25,"WNW"],
    [303.75,"NW"],
    [326.25,"NNW"],
    [348.75,"N"]
]
husoku = [
    0.2,1.5,3.3,5.4,7.9,10.7,13.8,17.1,20.7,24.4,28.4,32.6,32.8
]
cnt = 0
dir = ''
w = -1
print(deg)
while cnt <= len(hougaku)-1:
    if len(hougaku)-1 <= cnt:
        if hougaku[cnt][0] <= deg:
            dir = hougaku[cnt][1]
    else:
        if hougaku[cnt][0] <= deg < hougaku[cnt + 1][0]:
            dir = hougaku[cnt][1]
    cnt+=1
cnt = 0
dis = round(dis / 60, 2)
s = 0
e = husoku[0]
while cnt <= len(husoku)-1:
    if(dis <= husoku[0]):
        dir = 'C'
        w = 0
        break
    else:
        print("{0} <= {1} <= {2}, {3}".format(s,dis,e,cnt + 1))
        if s <= dis <= e:
            w = cnt + 1
            break
        s = round(e + 0.1, 2)
        cnt+=1
        e = husoku[cnt]
print("{0} {1}".format(dir, w))
