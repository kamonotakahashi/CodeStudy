#encoding: utf-8
import sys
TRUE = 1
FALSE = 0
def search(c, ary):
    for l in ary:
        if c in l:
            return TRUE
    return FALSE


W = input()
if not 1 <= len(W) <= 30:
    sys.exit()
list = ['a','i','u','e','o']
put = ''
for i in range(0,len(W)):
    if search(W[i], list) != 1:
        put = put + W[i]
print(put)
