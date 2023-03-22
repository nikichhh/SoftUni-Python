a = float(input())
b = int(input())
c = float(input())

a-=a*0.1
clothes = b*c

if b>150:
    clothes-=clothes*0.1

a-=clothes

if a<0:
    print("Not enough money!")
    print(f"Wingard needs {-a:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {a:.2f} leva left.")