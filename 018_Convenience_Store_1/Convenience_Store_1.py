import numpy as np


N = int(input())
A = np.array(list(map(int, input().split(" "))))

a1 = sum(A == 100)
a2 = sum(A == 200)
a3 = sum(A == 300)
a4 = sum(A == 400)

count = 0
if a1 >= 1 and a4 >= 1:
    count += a1 * a4
if a2 >= 1 and a3 >= 1:
    count += a2 * a3

print(count)