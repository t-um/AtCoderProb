A, B = list(map(int, input().split(" ")))


tempA = A
tempB = B

while (tempA != tempB):
    if tempA < tempB:
        tempB -= tempA
    else:
        tempA -= tempB

print(tempA)
