control_number = int(input())

counter = 0
password = 0
fourth_num = False

for a in range (1, 10):
    for b in range (1, 10):
        for c in range (1, 10):
            for d in range (1, 10):
                needed_num = a*b + c*d

                if a < b and c > d and needed_num == control_number:
                    print(f"{a}{b}{c}{d}", end= " ")
                    counter += 1

                    if counter == 4:
                        password = 1000 * a + 100 * b + 10 * c + d
                        fourth_num = True

print("")

if fourth_num:
    print(f"Password: {password}")
else:
    print("No!")