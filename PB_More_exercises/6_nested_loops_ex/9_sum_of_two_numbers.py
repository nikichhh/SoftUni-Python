first_num = int(input())
sec_num = int(input())
magic_num = int(input())

combination_cnt = 0

for x in range (first_num,sec_num+1):
    for y in range (first_num, sec_num+1):
        combination_cnt += 1
        if x + y == magic_num:
            print(f"Combination N:{combination_cnt} ({x} + {y} = {magic_num})")
            exit()

print(f"{combination_cnt} combinations - neither equals {magic_num}")