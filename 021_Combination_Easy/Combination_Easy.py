def product(nums):
    res = 1
    for num in nums:
        res *= num
    return res


def comb(n, k):
    k = min(k, n - k)
    if k == 0:
        return 1
    elif k < 0:
        return 0

    top = product(list(range(n - k + 1, n + 1)))
    bottom = product(list(range(1, k + 1)))
    return top // bottom


n, r = list(map(int, input().split(" ")))

print(comb(n, r))