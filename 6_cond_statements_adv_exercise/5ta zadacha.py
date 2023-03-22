a = float(input())
b = input()

c = ""
d = ""

if a <=100:
    c = "Bulgaria"
    if b == "summer":
        d = "Camp"
        a-=a*0.7
    else:
        d = "Hotel"
        a-=a*0.3
elif a <= 1000:
    c = "Balkans"
    if b == "summer":
        d = "Camp"
        a -= a * 0.6
    else:
        d = "Hotel"
        a -= a * 0.2
else:
    c = "Europe"
    d = "Hotel"
    a -= a*0.1

print(f"Somewhere in {c}")
print(f"{d} - {a:.2f}")