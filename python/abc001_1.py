import sys

H1 = input()
H2 = input()
if not 0 <= H1 <= 2000:
    sys.exit()
if not 0 <= H2 <= 2000:
    sys.exit()

print(H1 - H2)
