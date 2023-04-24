##1st variation
nums = input().split()
reverse_nums = []

while nums:
    reverse_nums.append(nums.pop())

print(" ".join(reverse_nums))

##2nd variation
# nums = input().split()
# reverse_nums = []
# 
# for el in range(len(nums)):
#     reverse_nums.append(nums.pop())
# 
# print(" ".join(reverse_nums))
