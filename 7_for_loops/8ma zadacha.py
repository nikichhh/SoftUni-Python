import sys

n = int(input())

min_num = sys.maxsize
max_num = -sys.maxsize

for i in range (1, n+1):
    num = int(input())
    if num<min_num:
        min_num=num
    if num>max_num:
        max_num=num

print(f"Max number: {max_num}\nMin number: {min_num}")