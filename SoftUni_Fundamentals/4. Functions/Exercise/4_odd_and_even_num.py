def odd_even(list):
    odd_sum = 0
    even_sum = 0
    for i in range(len(list)):
        if list[i] % 2 == 1:
            odd_sum += list[i]
        else:
            even_sum += list[i]

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


num = input()
numbers = []
for i in num:
    numbers.append(int(i))

print(odd_even(numbers))