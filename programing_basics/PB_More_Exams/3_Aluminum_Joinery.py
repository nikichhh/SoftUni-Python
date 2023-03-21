joinery = int(input())
type_joinery = input()
delivery = input()

price = 0

if joinery < 10:
    print(f"Invalid order")
    exit()

if type_joinery == "90X130":
    price = joinery * 110
    if joinery > 30 and joinery <= 60:
        price -= price * 0.05
    elif joinery > 60:
        price -= price * 0.08

elif type_joinery == "100X150":
    price = joinery * 140
    if joinery > 40 and joinery <= 80:
        price -= price * 0.06
    elif joinery > 80:
        price -= price * 0.1

elif type_joinery == "130X180":
    price = joinery * 190
    if joinery > 20 and joinery <= 50:
        price -= price * 0.07
    elif joinery > 50:
        price -= price * 0.12

elif type_joinery == "200X300":
    price = joinery * 250
    if joinery > 25 and joinery <= 50:
        price -= price * 0.09
    elif joinery > 50:
        price -= price * 0.14

if delivery == "With delivery":
    price += 60

if joinery > 99:
    price -= price * 0.04

print(f"{price:.2f} BGN")