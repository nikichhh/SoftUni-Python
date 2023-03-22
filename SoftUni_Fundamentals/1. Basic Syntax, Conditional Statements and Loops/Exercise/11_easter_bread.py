budget = float(input())

flour_price = float(input())

egg_price = flour_price * 0.75

milk_1l = flour_price * 1.25

milk_250 = milk_1l / 4

bread_cost = flour_price + egg_price + milk_250

coloured_eggs = 0
total_breads = 0

while budget > bread_cost:
    budget -= bread_cost
    coloured_eggs += 3
    total_breads += 1
    if total_breads % 3 == 0:
        coloured_eggs -= total_breads - 2

print(f"You made {total_breads} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")