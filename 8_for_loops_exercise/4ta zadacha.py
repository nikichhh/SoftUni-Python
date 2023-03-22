age = int(input())
wash_price = float(input())
toy_price = int(input())

num_Eve = age//2
sum_Eve = 0

for i in range(1,num_Eve+1):
    sum_Eve+=i

money = sum_Eve * 10.00 - num_Eve * 1.00 + (num_Eve + age % 2) * toy_price

if money-wash_price>=0:
    print(f"Yes! {money-wash_price:.2f}")
else:
    print(f"No! {abs(money-wash_price):.2f}")