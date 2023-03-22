first_num = int(input())
sec_num = int(input())
third_num = int(input())

if first_num > sec_num and first_num > third_num:
    print(first_num)

elif sec_num > first_num and sec_num > third_num:
    print(sec_num)

elif third_num > first_num and third_num > sec_num:
    print(third_num)