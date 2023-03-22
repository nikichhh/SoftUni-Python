a = input()
b = float(input())

price = 0

if a == "Sofia":
    if 0<=b<=500:
        price = 5
        print(f"{b*price/100.0:.2f}")
    elif b<=1000:
        price = 7
        print(f"{b * price/100.0:.2f}")
    elif b<=10000:
        price = 8
        print(f"{b * price/100.0:.2f}")
    elif b>10000:
        price = 12
        print(f"{b * price/100.0:.2f}")
    else:
        print("error")
elif a == "Varna":
    if 0<=b<=500:
        price = 4.5
        print(f"{b*price/100.0:.2f}")
    elif b<=1000:
        price = 7.5
        print(f"{b * price/100.0:.2f}")
    elif b<=10000:
        price =10
        print(f"{b * price/100.0:.2f}")
    elif b>10000:
        price = 13
        print(f"{b * price/100.0:.2f}")
    else:
        print("error")
elif a == "Plovdiv":
    if 0<=b<=500:
        price = 5.5
        print(f"{b*price/100.0:.2f}")
    elif 500<=b<=1000:
        price = 8
        print(f"{b * price/100.0:.2f}")
    elif 1000<=b<=10000:
        price = 12
        print(f"{b * price/100.0:.2f}")
    elif b>10000:
        price = 14.5
        print(f"{b * price/100.0:.2f}")
    else:
        print("error")
else:
    print("error")