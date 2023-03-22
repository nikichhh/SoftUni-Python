a = float(input())

b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

priceB = b*2.6
priceC = c*3
priceD = d*4.1
priceE = e*8.2
priceF = f*2

price = priceF+priceE+priceD+priceC+priceB

if b+c+d+e+f>=50:
    price-=price*0.25

price-=price*0.1

if price>=a:
    print(f"Yes! {price-a:.2f} lv left.")
else:
    print(f"Not enough money! {a-price:.2f} lv needed.")