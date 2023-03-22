numbers = [int(x) for x in input().split()]
count = int(input())

for _ in range(count):
    number_to_remove = min(numbers)
    numbers.remove(number_to_remove)
    # min_number = float('inf') another way to write this
    # for num in numbers:
    #     if num < min_number:
    #         min_number = num

print(", ".join(str(x) for x in numbers))
# for idx in range(len(numbers)): another way to write this
#     num = numbers[idx]
#     if idx == len(numbers) -1:
#         print(num)
#     else:
#         print(num, end=", ")
