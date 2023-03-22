def even(numbers):
    nums = []
    for i in numbers:
        if i % 2 == 0:
            nums.append(i)

    return nums


numbers = (int(x) for x in input().split())
print(even(numbers))
