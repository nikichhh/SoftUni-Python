import sys

a = input()

max_num = -sys.maxsize

while a != "Stop":
    num = int(a)
    if num>max_num:
        max_num=num
    a = input()

print(max_num)