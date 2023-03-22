n_num = int(input())
l_num = int(input())

letter = 97 + l_num

for a in range (1, n_num):
    for b in range (1, n_num):
        for c in range (97, letter):
            for d in range (97, letter):
                for e in range (1, n_num + 1):
                    if e > a and e > b:
                        print(f"{a}{b}{chr(c)}{chr(d)}{e}", end=" ")