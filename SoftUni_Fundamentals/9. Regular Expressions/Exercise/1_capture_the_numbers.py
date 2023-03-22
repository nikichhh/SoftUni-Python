import re

nums = []

while True:
    line = input()
    if not line:
        break

    pattern = r"\d+"

    nums.extend(re.findall(pattern, line))

print(*nums, sep=" ")
