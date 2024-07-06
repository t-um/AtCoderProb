N, S = list(map(int, input().split(" ")))

num = 0
for i in range(1, N + 1):
    num += max(min(S - i, N), 0)

print(num)