import numpy as np
import math

N = int(input())
A = list(map(int, input().split(" ")))

temp = np.zeros(100001, dtype=np.int32)
for a in A:
    temp[a] += 1

diff = temp[50000] * temp[50000] / 2 - math.comb(temp[50000], 2)

print(int(np.sum(temp * np.flip(temp)) / 2 - diff))
