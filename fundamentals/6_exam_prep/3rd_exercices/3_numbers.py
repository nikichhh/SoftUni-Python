nums = [int(x) for x in input().split()]

average_score = sum(nums) / len(nums)

max_nums = []
for i in range(len(nums)):
    if nums[i] > average_score:
        max_nums.append(nums[i])

if len(max_nums) > 5:
    while len(max_nums) != 5:
        max_nums.remove(min(max_nums))

max_nums.sort(reverse=True)

if len(max_nums) == 0:
    print("No")
else:
    print(*max_nums, sep=" ")
