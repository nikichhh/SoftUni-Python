import sys

n = int(input())

max_num = -sys.maxsize

sum_all = 0

for i in range (1,n+1):
    num = int(input())
    if num>max_num:
        max_num=num
    sum_all+=num

sum_all -= max_num

if sum_all == max_num:
    print(f"Yes\nSum = {max_num}")
else:
    print(f"No\nDiff = {abs(sum_all-max_num)}")