collection_of_items = input().split("|")
budget = int(input())

budget_first = budget
budget_profit = 0
new_price = []
# is_going = False

for collection in collection_of_items:
    args = collection.split("->")
    cloth_type = args[0]
    price = float(args[1])
    valid = False

    if budget < price:
        continue

    if cloth_type == "Clothes":
        if price <= 50:
            valid = True
    elif cloth_type == "Shoes":
        if price <= 35:
            valid = True
    elif cloth_type == "Accessories":
        if price <= 20.5:
            valid = True

    if valid:
        budget -= price
        price += price * 0.4
        new_price.append(price)
        budget_profit += price

# print(f"{new_price:.2f}") not working
for idx in range(len(new_price)):
    newer_price = new_price[idx]
    print(f"{newer_price:.2f}", end=(" "))
print(f"\nProfit: {budget_profit + budget - budget_first:.2f}")
if budget_profit + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")