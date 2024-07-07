def calc_gcd(x, y):
    while (x != y):
        if x < y:
            y = y % x
            if y == 0:
                return x
        else:
            x = x % y
            if x == 0:
                return y
    return x


def calc_lcm(x, y):
    return x * y // calc_gcd(x, y)


def lcm_of_list(A):
    res = A[0]
    for a in A[1:]:
        res = calc_lcm(res, a)
    return res


N = int(input())
A = list(map(int, input().split(" ")))
print(lcm_of_list(A))
