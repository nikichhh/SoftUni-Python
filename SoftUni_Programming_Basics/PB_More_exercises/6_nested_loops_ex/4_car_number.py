first_digit = int(input())
second_digit = int(input())

for n1 in range (first_digit, second_digit + 1):
    for n2 in range(first_digit, second_digit + 1):
        for n3 in range(first_digit, second_digit + 1):
            for n4 in range(first_digit, n1):

                if n1 > n4:
                    if n1 % 2 == 0:
                        if n4 % 2 != 0:
                            if (n1 - n4) % 2 != 0 and (n2 + n3) % 2 == 0:
                                print(f"{n1}{n2}{n3}{n4}", end= " ")
                    else:
                        if n4 % 2 == 0:
                            if (n1 - n4) % 2 != 0 and (n2 + n3) % 2 == 0:
                                print(f"{n1}{n2}{n3}{n4}", end= " ")