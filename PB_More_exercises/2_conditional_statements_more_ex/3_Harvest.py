import math

x = int(input())
y = float(input())
z = int(input())
people_needed = int(input())

grozde = x * y
wine = 0.4 * grozde / 2.5

if wine >= z:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(wine - z)} liters left -> {math.ceil((wine - z) / people_needed)} liters per person.")

else:
    print(f"It will be a tough winter! More {math.floor(z - wine)} liters wine needed.")