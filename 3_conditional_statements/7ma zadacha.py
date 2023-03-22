import math

a = input()
b = float(input())

if a == "square":
    print(f"{b**2:.3f}")
elif a == "rectangle":
    c = float(input())
    print(f"{b*c:.3f}")
elif a == "circle":
    print(f"{(b**2)*math.pi:.3f}")
else:
    c = float(input())
    print(f"{b*c/2:.3f}")