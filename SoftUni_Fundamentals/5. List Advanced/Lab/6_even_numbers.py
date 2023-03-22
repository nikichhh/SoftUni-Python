nums = [int(x) for x in input().split(", ")]

print([el for el in range(len(nums)) if nums[el] % 2 == 0])
