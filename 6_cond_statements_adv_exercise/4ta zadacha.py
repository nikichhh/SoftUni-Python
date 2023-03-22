a = int(input())
b = input()
c = int(input())

if b == "Spring":
    d = 3000
    if c <= 6:
        d -= d * 0.1
    elif c <= 11:
        d -= d * 0.15
    elif c >= 12:
        d -= d * 0.25
    if c%2==0:
        d-=d*0.05

elif b == "Summer" or b == "Autumn":
    d = 4200
    if c <= 6:
        d -= d * 0.1
    elif c <= 11:
        d -= d * 0.15
    elif c >= 12:
        d -= d * 0.25
    if c % 2 == 0 and b == "Summer":
        d -= d * 0.05
else:
    d = 2600
    if c <= 6:
        d -= d * 0.1
    elif c <= 11:
        d -= d * 0.15
    elif c >= 12:
        d -= d * 0.25
    if c % 2 == 0:
        d -= d * 0.05

if a>=d:
    print(f"Yes! You have {a-d:.2f} leva left.")
else:
    print(f"Not enough money! You need {d-a:.2f} leva.")

