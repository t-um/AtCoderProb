import numpy as np

num = int(input())

group_num = np.min((100000, int(np.ceil(np.sqrt(num)))))
check_num = int(np.ceil(np.sqrt(num) / group_num))
start = 2
is_prime = True

for i in range(check_num):
    check_group = np.array(list(range(start, start + group_num)))
    if num < 10:
        check_group = check_group[check_group < num]
    if sum(num % check_group == 0) > 0:
        is_prime = False
        break
    
    start += group_num

if is_prime:
    print("Yes")
else:
    print("No")