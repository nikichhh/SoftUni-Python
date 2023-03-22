d1 = int(input())
d2 = int(input())

for number in range (d1,d2+1):
    number_to_str = str(number)
    evn = 0
    odd = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            evn += int(digit)
        else:
            odd += int(digit)

    if evn == odd:
        print(number, end = ' ')