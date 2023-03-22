import sys

a = input()

min_num = sys.maxsize

while a != "Stop":
    num = int(a)
    if num<min_num:
        min_num=num
    a = input()

print(min_num)