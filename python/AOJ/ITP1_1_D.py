S = int(input())
h = int(S/3600) if 9 < int(S/3600) else int(S/3600)
m = int(S/60) % 60 if 9 < int(S/60) % 60 else int(S/60) % 60
s = S % 60 if 9 < S % 60 else S % 60
print("{0}:{1}:{2}".format(h, m, s))