import sys
import re
inp = []
for cnt in range(2):
  inp.append(input())
  if not 1 <= len(inp[cnt]) <= 10:
    sys.exit()
  if not re.match(r"^[a-z]+$", inp[cnt]):
    sys.exit()

if len(inp[0]) < len(inp[1]):
  if(inp[0] == inp[1][:-1]):
    print("Yes")
    sys.exit()
print("No")