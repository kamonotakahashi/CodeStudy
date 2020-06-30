import re
import sys
S = input()
T = input()
w = 0
if not re.match(r'^[a-z]+$', S) or not re.match(r'^[a-z]+$', T) or len(S) != len(T) or (10 ** 5 * 2) < len(S):
  sys.exit()
if S != T:
  i = 0
  for l in S:
    if l != T[i]:
      w = w + 1
    i = i + 1
print(w)