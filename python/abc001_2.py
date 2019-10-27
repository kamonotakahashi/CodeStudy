import sys
m = input()
if not 0 <= m <= 100000:
    sys.exit()
km = m * 0.001

if km < 0.1:
    c = str('00')
elif 0.1 <= km <= 5:
    c = str(int(km * 10)) if 10 <= (km * 10) else '0' + str(int(km * 10))
elif 6 <= km <= 30:
    c = str(int(km + 50))
elif 35 <= km <= 70:
    c = str(int((km - 30)/5 + 80))
elif 70 < km:
    c = str(89)

print(c)
