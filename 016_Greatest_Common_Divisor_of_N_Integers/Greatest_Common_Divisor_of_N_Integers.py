import numpy as np


N = int(input())
A = np.array(list(map(int, input().split(" "))))

while min(A) != max(A):
    # 各値に対して何回引いてよいか算出
    min_num = min(A)
    sub = (A[A != min_num] - min_num) // min_num

    # 最低でも1回は引く
    sub = np.array(list(map(lambda x: max(1, x), sub)))

    A[A != min_num] -= sub * min_num

print(min(A))
