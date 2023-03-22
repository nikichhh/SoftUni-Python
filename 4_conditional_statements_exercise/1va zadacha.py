import math

a = int(input())
b = int(input())
c = int(input())

sum_seconds = a+b+c

minutes = sum_seconds//60
seconds = sum_seconds%60

minutes = math.floor(minutes)

if seconds<10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")