one_lev = int(input())
two_lev = int(input())
five_lev = int(input())
wanted = int(input())

for i in range (0, one_lev + 1):
    for j in range (0, two_lev + 1):
        for k in range(0, five_lev + 1):
            if i * 1 + j * 2 + k * 5 == wanted:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {wanted} lv.")