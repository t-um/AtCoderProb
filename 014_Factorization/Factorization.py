import numpy as np


N = int(input())

prime = []

# 素因数分解
while N > 1:
    num = int(np.floor(np.sqrt(N)))
    is_found = False
    for i in range(2, num + 1):
        if N % i == 0:
            prime.append(i)
            N = N // i
            is_found = True
            break
    if not is_found:
        prime.append(N)
        N = 1

print(*prime)