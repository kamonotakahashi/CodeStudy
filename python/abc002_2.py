#encoding: utf-8
import sys
TRUE = 1
FALSE = 0
def search(c, ary):
    for l in ary:
        if c in l:
            return TRUE
    return FALSE

list = ['a','i','u','e','o']
alphabet = [chr(i) for i in range(97, 97+26)]
W = input()
put = ''
hitCnt = 0
if not 1 <= len(W) <= 30:
    sys.exit()

for i in range(0,len(W)):
    if search(W[i], list) != 1:
        put = put + W[i]
        hitCnt = hitCnt+1
    if search(W[i], alphabet) != 1:
        sys.exit()

if hitCnt < 1:
    sys.exit()
print(put)
