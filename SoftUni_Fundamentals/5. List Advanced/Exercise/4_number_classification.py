nums = [int(x) for x in input().split(", ")]

positive = []
negative = []
even = []
odd = []
for num in nums:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Positive: ", end=", ".join(str(x) for x in positive))
print("\nNegative: ", end=", ".join(str(x) for x in negative))
print("\nEven: ", end=", ".join(str(x) for x in even))
print("\nOdd: ", end=", ".join(str(x) for x in odd))

# positive = [i for i in nums if i >= 0]
# negative = [i for i in nums if i < 0]
# even = [i for i in nums if i % 2 == 0]
# odd = [i for i in nums if i % 2 != 0]
