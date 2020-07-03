import re

def parser(s):
  m = re.match(r'^\s*([\d]{0,}[a-z]{0,})\s*(\+|\-|\*|\/)\s*([\d]{0,}[a-z]{0,})\s*\=\s*[\d]{1,}\s*', s)
  t = []
  for l in m.group():
    if re.match(r'[^\s]'. str(l)):
      t.append(l)
  return t

str = "2x + 4y = 8"
c = parser(str)
for cc in c:
  print(cc)
