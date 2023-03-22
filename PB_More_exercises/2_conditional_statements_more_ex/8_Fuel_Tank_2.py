# fuel = input()
# tank_fuel = float(input())
# card = input()
#
# types = ["Gas", "Gasoline", "Diesel"]
# price = 0
#
# if fuel == types[0]:
#     price = tank_fuel * 0.93
#     if card == "Yes":
#         price -= tank_fuel * 0.08
# elif fuel == types[1]:
#     price = tank_fuel * 2.22
#     if card == "Yes":
#         price -= tank_fuel * 0.18
# else:
#     price = tank_fuel * 2.33
#     if card == "Yes":
#         price -= tank_fuel * 0.12
#
# if 20 <= tank_fuel <= 25:
#     price -= price * 0.08
# elif tank_fuel > 25:
#     price -= price * 0.1
#
# print(f"{price:.2f} lv.")

budget = int(input())
season = input()
count_people = int(input())

price = 0
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if count_people <= 6:
    price = price * 0.9

elif 6 < count_people <= 11:
    price = price * 0.85

elif count_people > 11:
    price = price * 0.75

if count_people % 2 == 0 and season != 'Autumn':
    price = price * 0.95

diff = abs(budget - price)
if budget >= price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')