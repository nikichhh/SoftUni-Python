nums = (float(x) for x in input().split())

occurrence = {}

for num in nums:
    if num not in occurrence:
        occurrence[num] = 0
    occurrence[num] += 1

[print(f"{num} - {value} times") for num, value in occurrence.items()]
