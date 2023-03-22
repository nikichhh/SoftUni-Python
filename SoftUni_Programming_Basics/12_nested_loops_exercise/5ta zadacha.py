n = int(input())

for i in range (1, 10):
    for j in range (1, 10):
        for k in range (1, 10):
            for l in range (1, 10):
                is_valid = n % i == 0 and n % j == 0 and n % k == 0 and n % l == 0
                if is_valid:
                    print(f"{i}{j}{k}{l}", end=" ")

# for i in range (1111,10000):
#     copy = i
#     is_true = True
#
#     while int(copy) != 0:
#         if copy % 10 == 0:
#             is_true = False
#             break
#         elif n % (copy % 10) != 0:
#             is_true = False
#             break
#         copy //= 10
#
#     if is_true == True:
#         print(i, end = " ")