price = float(input())

price *= 100

coin_cnt = 0

while int(price) > 0:
    price = int(price)
    if price - 200 >= 0:
        price -= 200
        coin_cnt += 1
    elif price - 100 >= 0:
        price -= 100
        coin_cnt += 1
    elif price - 50 >= 0:
        price -= 50
        coin_cnt += 1
    elif price - 20 >= 0:
        price -= 20
        coin_cnt += 1
    elif price - 10 >= 0:
        price -= 10
        coin_cnt += 1
    elif price - 5 >= 0:
        price -= 5
        coin_cnt += 1
    elif price - 2 >= 0:
        price -= 2
        coin_cnt += 1
    elif price == 1:
        price -= 1
        coin_cnt += 1

print(coin_cnt)