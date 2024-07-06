import numpy as np


N, S = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

# 動的計画法
# ・n枚目のカードまでで合計が
# 「dp == Trueとなるindex + 1」となる組み合わせが存在
# ・最終的にdp[S - 1]がTrueとなっていれば合計Sとなる組み合わせが存在
dp = np.full(S, False)

for i in range(N):
    prev = np.where(dp)[0]
    # 過去との組み合わせ
    if len(prev) > 0:
        curr = prev + A[i]
        dp[curr[curr < S]] = True

    # 現在のカード単体
    if A[i] - 1 < S:
        dp[A[i] - 1] = True

if dp[S - 1]:
    print("Yes")
else:
    print("No")