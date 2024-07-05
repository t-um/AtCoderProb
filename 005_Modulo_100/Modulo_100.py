input()  # 無視
nums = input().split(" ")
num_sum = 0
for num in nums:
    num_sum += int(num)

print(num_sum % 100)