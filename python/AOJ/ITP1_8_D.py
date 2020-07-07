s = str(input())
p = str(input())
m = s + s[0:-1]
if 0 <= m.find(p):
    print('Yes')
else:
    print('No')