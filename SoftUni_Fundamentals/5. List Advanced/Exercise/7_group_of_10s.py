# from math import ceil

nums = [int(x) for x in input().split(", ")]

new_nums = []
count = 1
while len(nums) != 0:
    new_nums = []
    for num in nums:
        if num <= count * 10:
            new_nums.append(num)
    for numbers in new_nums:
        nums.remove(numbers)

    print(f"Group of {count * 10}'s: {new_nums}")
    count += 1

# groups_count = ceil(max(nums) / 10)
# lowest_boundery = 1
# highest_boundery = 10
# for idx in range(1, groups_count + 1):
#     grouped_numbers = [x for x in nums if lowest_boundery <= x <= highest_boundery]
#     print(f"Group of {idx * 10}'s: {grouped_numbers}")
#
#     lowest_boundery += 10
#     highest_boundery += 10