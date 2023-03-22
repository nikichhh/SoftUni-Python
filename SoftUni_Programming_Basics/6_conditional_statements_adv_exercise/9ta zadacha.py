a = int(input())
b = input()
c = input()

price = 0

if b == "room for one person":
    price = (a-1)*18
elif b == "apartment":
    price = (a-1)*25
    if a<10:
        price-=price*0.3
    elif a<=15:
        price-=price*0.35
    else:
        price/=2
else:
    price = (a-1)*35
    if a<10:
        price-=price*0.1
    elif a<=15:
        price-=price*0.15
    else:
        price-=price*0.2

if c == "positive":
    price+=price*0.25
else:
    price-=price*0.1

print(f"{price:.2f}")