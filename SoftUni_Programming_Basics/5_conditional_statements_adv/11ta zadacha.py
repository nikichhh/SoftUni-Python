a = input()
b = input()
c = float(input())

price = 0

if a == "banana":
    if b == "Monday" or b == "Tuesday" or b == "Wednesday" or b == "Thursday" or b == "Friday":
        price = 2.5
        print(f"{price * c:.2f}")
    elif b == "Saturday" or b == "Sunday":
        price = 2.70
        print(f"{price * c:.2f}")
    else:
        print("error")
elif a == "apple":
    if b == "Monday" or b == "Tuesday" or b == "Wednesday" or b == "Thursday" or b == "Friday":
        price = 1.2
        print(f"{price * c:.2f}")
    elif b == "Saturday" or b == "Sunday":
        price = 1.25
        print(f"{price * c:.2f}")
    else:
        print("error")
elif a == "orange":
    if b == "Monday" or b == "Tuesday" or b == "Wednesday" or b == "Thursday" or b == "Friday":
        price = 0.85
        print(f"{price * c:.2f}")
    elif b == "Saturday" or b == "Sunday":
        price = 0.9
        print(f"{price * c:.2f}")
    else:
        print("error")
elif a == "grapefruit":
    if b == "Monday" or b == "Tuesday" or b == "Wednesday" or b == "Thursday" or b == "Friday":
        price = 1.45
        print(f"{price * c:.2f}")
    elif b == "Saturday" or b == "Sunday":
        price = 1.60
        print(f"{price * c:.2f}")
    else:
        print("error")
elif a == "kiwi":
    if b == "Monday" or b == "Tuesday" or b == "Wednesday" or b == "Thursday" or b == "Friday":
        price = 2.7
        print(f"{price * c:.2f}")
    elif b == "Saturday" or b == "Sunday":
        price = 3
        print(f"{price * c:.2f}")
    else:
        print("error")
elif a == "pineapple":
    if b == "Monday" or b == "Tuesday" or b == "Wednesday" or b == "Thursday" or b == "Friday":
        price = 5.5
        print(f"{price * c:.2f}")
    elif b == "Saturday" or b == "Sunday":
        price = 5.6
        print(f"{price * c:.2f}")
    else:
        print("error")
elif a == "grapes":
    if b == "Monday" or b == "Tuesday" or b == "Wednesday" or b == "Thursday" or b == "Friday":
        price = 3.85
        print(f"{price * c:.2f}")
    elif b == "Saturday" or b == "Sunday":
        price = 4.2
        print(f"{price * c:.2f}")
    else:
        print("error")
else:
    print("error")