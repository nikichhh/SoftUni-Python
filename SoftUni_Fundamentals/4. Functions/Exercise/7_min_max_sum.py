def solve(numbers):
    return f"The minimum number is {min(numbers)}\n" \
           f"The maximum number is {max(numbers)}\n" \
           f"The sum number is: {sum(numbers)}"


numbers = (int(x) for x in input().split())
nums = []
for i in numbers:
    nums.append(i)
print(solve(nums))
