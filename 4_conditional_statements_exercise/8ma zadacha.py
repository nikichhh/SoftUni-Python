from math import ceil
a = input()
b = int(input())
c = int(input())

first = c/8
second = c/4 + first
c-=second

if c>=b:
    print(f"You have enough time to watch {a} and left with {ceil(c-b)} minutes free time.")
else:
    print(f"You don't have enough time to watch {a}, you need {ceil(b-c)} more minutes.")