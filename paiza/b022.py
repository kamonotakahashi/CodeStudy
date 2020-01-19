#encoding: utf-8
import sys

N = int(input())
es = ["s","o","x","sh","ch"]
ves = ["f","fe"]
ies = ["y"]
nies = ["ay","iy","uy","ey","oy"]

if not 1 <= N <= 10:
    sys.exit()
a = [chr(i) for i in range(97, 97+26)]

def chk_alpha(alphabet, a):
    length = len(alphabet)
    i = 0
    flg = 0
    hit = 0
    for l in alphabet:
        while(1):
            if len(a) <= i:
                flg = -1
                break
            if l in a[i]:
                hit = hit + 1
                break
            else:
                i = i + 1
        if length <= hit:
            flg = 1
            break
        if flg == -1:
            break
        i = 0
    return flg

def chk_t(alphabet, ary):
    i = 0
    t = ''
    flg = 0
    hit = ''
    while(1):
        if len(ary) - 1 < i:
            break
        c = ary[i]
        if len(c) == 2:
            t = alphabet[len(alphabet) - 2:]
        else:
            t = alphabet[len(alphabet) - 1:]
        if t in c:
            flg = 1
            hit = c
            break
        i = i + 1
    return [flg,hit]

def change_tango(alphabet):
    ans = chk_t(alphabet, es)
    if ans[0] == 1:
        return alphabet + "es"
    ans = chk_t(alphabet, ves)
    if ans[0] == 1:
        return alphabet.replace(ans[1], "ves")
    ans = chk_t(alphabet, ies)
    ans2 = chk_t(alphabet, nies)
    if ans[0] == 1 and ans2[0] != 1:
        return alphabet.replace(ans[1], "ies")
    return alphabet + "s"

buf = []
for i in range(0, N):
    tango = str(input())
    if not 2 <= len(tango) <= 20:
        sys.exit()
    if not chk_alpha(tango, a) == 1:
        sys.exit()
    buf.append(change_tango(tango))
for l in buf:
    print(l)
