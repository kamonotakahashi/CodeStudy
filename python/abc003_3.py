#encoding: utf-8
#
# https://atcoder.jp/contests/abc003/tasks/abc003_3
# C - AtCoderプログラミング講座
#

import sys
io = input().split(' ')
N = int(io[0])
K = int(io[1])

if not (1 <= N <= 100) or not (1 <= K <= N):
    sys.exit()
