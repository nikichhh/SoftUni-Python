hour = int(input())
day_week = input()

if hour >=10 and hour<=18:
    if day_week == "Sunday":
        print("closed")
    else:
        print("open")
else:
        print("closed")