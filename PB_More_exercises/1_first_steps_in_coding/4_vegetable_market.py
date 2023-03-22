price_vegetables = float(input())
price_fruits = float(input())
weight_vegetables = int(input())
weight_fruits = int(input())

print(f"{(price_fruits * weight_fruits + price_vegetables * weight_vegetables) / 1.94:.2f}")