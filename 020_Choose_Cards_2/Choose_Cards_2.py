import numpy as np

N = int(input())
A = np.array(list(map(int, input().split(" "))))

# [選んだカードの枚数, 合計値]
dp = np.zeros((5, 1000), dtype=np.int32)

for a in A:
    next_num = np.where(dp > 0)[0] + 1
    next_val = np.where(dp > 0)[1] + a
    valid_idx = np.logical_and(next_num < 5, next_val < 1000)
    dp[next_num[valid_idx], next_val[valid_idx]] += dp[np.where(dp > 0)][valid_idx]

    dp[0, a - 1] += 1

print(int(dp[4, 999]))
