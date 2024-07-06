import numpy as np


def add_factor(pf, factor):
    if factor not in pf:
        pf[factor] = 1
    else:
        pf[factor] += 1
    return pf


def prime_factorization(N):
    pf = {}

    # 素因数分解
    while N > 1:
        num = int(np.floor(np.sqrt(N)))
        is_found = False
        for i in range(2, num + 1):
            if N % i == 0:
                pf = add_factor(pf, i)
                N = N // i
                is_found = True
                break
        if not is_found:
            pf = add_factor(pf, N)
            N = 1

    return pf


def calc_lcm(x, y):
    pf_x = prime_factorization(x)
    pf_y = prime_factorization(y)

    lcm = 1
    # 素因数を最小公倍数となるようにマージ
    for key in (pf_x.keys() | pf_y.keys()):
        if key in pf_x and key in pf_y:
            lcm *= (key ** max(pf_x[key], pf_y[key]))
        elif key in pf_x:
            lcm *= (key ** pf_x[key])
        else:
            lcm *= (key ** pf_y[key])

    return lcm


def main():
    N, X, Y = list(map(int, input().split(" ")))

    # XとYの最小公倍数を求める
    lcm = calc_lcm(X, Y)

    if Y % X == 0:
        print(N // X)
    else:
        print(N // X + N // Y - N // (lcm))


if __name__ == "__main__":
    main()