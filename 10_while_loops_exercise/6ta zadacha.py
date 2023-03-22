a = int(input())
b = int(input())

cake = a*b

taken_parts = input()

while taken_parts != "STOP" and cake >= 0:
    cake -= int(taken_parts)
    if cake < 0:
        print(f"No more cake left! You need {abs(cake)} pieces more.")
        exit()
    taken_parts = input()

print(f"{cake} pieces are left.")