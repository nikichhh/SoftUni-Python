budget = int(input())
price = input()

while price != "End":
    budget -= int(price)

    if budget < 0:
        print(f"You went in overdraft!")
        exit()

    price = input()

print(f"You bought everything needed.")