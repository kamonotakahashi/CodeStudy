in_ = list(map(int, input().split(' ')))
N = in_[0]
K = in_[1]
p = list(map(int, input().split(' ')))
p.sort()
print(sum(p[0:K]))