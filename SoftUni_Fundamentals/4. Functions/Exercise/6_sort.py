def sort_it(numbers):
    return sorted(numbers)


numbers = (int(x) for x in input().split())
print(sort_it(numbers))