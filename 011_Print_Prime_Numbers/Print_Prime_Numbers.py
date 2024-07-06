import numpy as np


N = int(input())

prime = np.array([2])

for i in range(2, N + 1):
    if np.all(i % prime != 0):
        prime = np.append(prime, i)

for i in range(len(prime)):
    print(prime[i])