a = input()

sum = 0

while a != "NoMoreMoney":
    if float(a)<0:
        print("Invalid operation!")
        break
    sum+=float(a)
    print(f"Increase: {float(a):.2f}")
    a = input()

print(f"Total: {sum:.2f}")