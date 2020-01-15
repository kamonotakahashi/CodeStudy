#encoding: utf-8
#
# https://atcoder.jp/contests/abc002/tasks/abc002_4
# D - 派閥
#

import sys
import math
TRUE = 1
FALSE = 0
def search(c, ary):
    for l in ary:
        if c == l:
            return TRUE
    return FALSE

io = input().split(' ')
N = int(io[0])
M = int(io[1])
A = {}
if not (1 <= N <= 12) or not (0 <= M <= math.floor((N*N-N)/2)):
    sys.exit()
for l in range(0, M):
    io = input().split(' ')
    X = int(io[0])
    Y = int(io[1])
    Xkey = "_" + str(io[0])
    Ykey = "_" + str(io[1])

    if not Xkey in A:
        A[Xkey] = []
    if not Ykey in A:
        A[Ykey] = []

    if search(Y, A[Xkey]) != 1:
        A[Xkey].append(Y)
    if search(X, A[Ykey]) != 1:
        A[Ykey].append(X)

    if not (1 <= X < Y <= N):
        sys.exit()

max = 0
maxPairCnt = 0
for key in A:
    if max < len(A[key]):
        max = len(A[key])
for key in A:
    if(max == len(A[key])):
        maxPairCnt = maxPairCnt + 1
if maxPairCnt == 0:
    maxPairCnt = 1
print(maxPairCnt)
