screen_type = input()
rows = int(input())
colums = int(input())

if screen_type == "Premiere":
    income = rows*colums*12
elif screen_type == "Normal":
    income = rows*colums*7.5
else:
    income = rows * colums * 5

print(f"{income:.2f} leva")