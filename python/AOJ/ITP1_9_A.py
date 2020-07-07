tg = str(input())
cnt = 0
while True:
    t = str(input())
    p = 0
    if t == 'END_OF_TEXT':
        break
    for a in t.split(' '):
        if a.lower() == tg:
            cnt += 1
print(cnt)