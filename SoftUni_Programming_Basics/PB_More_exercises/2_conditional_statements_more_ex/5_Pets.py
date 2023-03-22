import math

days = int(input())
left_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

food = days * (dog_food + cat_food + turtle_food / 1000)

if left_food >= food:
    print(f"{math.floor(left_food - food)} kilos of food left.")
else:
    print(f"{math.ceil(food - left_food)} more kilos of food are needed.")