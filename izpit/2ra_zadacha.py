tshirt_price = float(input())
wanted_price = float(input())

shorts_price = tshirt_price * 0.75
chorapi_price = shorts_price * 0.2
shoes_price = (shorts_price + tshirt_price) * 2

all_price = tshirt_price + shoes_price + chorapi_price + shorts_price
all_price -= all_price * 0.15

if all_price >= wanted_price:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {all_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {wanted_price - all_price:.2f} lv. more.")