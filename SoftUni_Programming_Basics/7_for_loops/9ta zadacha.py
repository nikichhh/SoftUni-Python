n = int(input())

left_sum = 0
right_sum = 0

for i in range(0,n):
    num1 = int(input())
    left_sum+=num1

for x in range(0,n):
    num2 = int(input())
    right_sum += num2

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")