n = int(input())
a = list(map(int, input().split(' ')))
print("{0} {1} {2}".format(min(list(map(int, a))), max(list(map(int, a))), sum(list(map(int, a)))))