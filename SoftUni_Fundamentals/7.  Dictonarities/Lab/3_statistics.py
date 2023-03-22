products = {}

command = input()

while command != 'statistics':
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])

    if product not in products:
        products[product] = 0

    products[product] += quantity

    command = input()

print('Products in stock:')
for (product, quantity) in products.items():
    print(f'- {product}: {quantity}')
# [print(f"- {product}: {quantity}" for (product, quantity) in products)]
print(f"Total Products: {len(products.keys())}\nTotal Quantity: {sum(products.values())}")
