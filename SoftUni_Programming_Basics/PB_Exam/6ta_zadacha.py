# n = int(input())
#
# num_reach = False
# count = 0
#
# for a in range (1, 10):
#     for b in range (9, a, -1):
#         for c in range (0, 10):
#             for d in range (9, c, -1):
#                 if (a + b + c + d) == (a*b*c*d) and n % 10 == 5:
#                     count += 1
#                     print(f"{a}{b}{c}{d}")
#                     number_reach = True
#                     break
#                 elif (a*b*c*d)//(a+b+c+d) == 3 and n % 3 == 0:
#                     count += 1
#                     print(f"{d}{c}{b}{a}")
#                     number_reach = True
#                     break
#             if number_reach == True:
#                 break
#         if number_reach == True:
#                 break
#     if number_reach == True:
#                 break
# if count == 0:
#     print("Nothing found")

n_number = int(input())

number_reach = False
count = 0

for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(0, 10):
            for d in range(9, c, -1):
                num_sum = a + b + c + d
                num_mult = a * b * c * d
                if num_sum == num_mult and n_number % 10 == 5:
                    count += 1
                    print(f'{a}{b}{c}{d}')
                    number_reach = True
                    break
                elif num_mult // num_sum == 3 and n_number % 3 == 0:
                    count += 1
                    print(f'{d}{c}{b}{a}')
                    number_reach = True
                    break
            if number_reach:
                break
        if number_reach:
            break
    if number_reach:
        break
if count == 0:
    print("Nothing found")
