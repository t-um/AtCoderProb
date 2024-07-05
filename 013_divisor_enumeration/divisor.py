import numpy as np


def main():
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

    divisor = []
    # 素因数分解結果を掛けて約数を表示
    for i in range(2**len(prime)):
        i_bin = list(map(int, list(f'{i:b}')))
        i_bin = [0 for i in range(len(prime) - len(i_bin))] + i_bin
        select_idx = np.where(i_bin)[0]
        temp = np.prod(np.array(prime, dtype=np.int64)[select_idx])
        if temp not in divisor:
            divisor.append(temp)

    for num in divisor:
        print(num)


if __name__=="__main__":
    main()