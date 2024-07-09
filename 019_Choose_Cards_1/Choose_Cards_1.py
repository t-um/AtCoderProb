import numpy as np


def comb(n, k):
    k = min(k, n - k)
    if k == 0:
        return 1
    elif k < 0:
        return 0
    top = np.arange(n - k, n) + 1
    bottom = np.arange(k) + 1
    return int(np.prod(top) / np.prod(bottom))

N = int(input())
A = np.array(list(map(int, input().split(" "))))


r = sum(A == 1)
y = sum(A == 2)
b = sum(A == 3)

print(comb(r, 2) + comb(y, 2) + comb(b, 2))