numbers = input()
nums = numbers.split()

for k in range(0, len(nums)):
    nums[k] = int(nums[k])

for i in range(len(nums)):
    nums[i] = nums[i] * (-1)

print(nums)
