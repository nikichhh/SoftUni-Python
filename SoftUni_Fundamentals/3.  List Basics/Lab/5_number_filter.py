n = int(input())

nums = []

for i in range(1, n + 1):
    number = int(input())
    nums.append(number)

command = input()

if command == "even":
    for k in range(len(nums) - 1, -1, -1):
        element = nums[k]
        if element % 2 != 0:
            nums.remove(element)
elif command == "odd":
    for k in range(len(nums) - 1, -1, -1):
        element = nums[k]
        if element % 2 == 0:
            nums.remove(element)
elif command == "negative":
    for k in range(len(nums) - 1, -1, -1):
        element = nums[k]
        if element >= 0:
            nums.remove(element)
elif command == "positive":
    for k in range(len(nums) - 1, -1, -1):
        element = nums[k]
        if element < 0:
            nums.remove(element)

print(nums)
