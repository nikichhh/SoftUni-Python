n = int(input())

total = 0

for i in range (n):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 <= price <= 100 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        print(f"The price for the coffee is: ${price * days * capsules:.2f}")
        total += price * days * capsules

print(f"Total: ${total:.2f}")