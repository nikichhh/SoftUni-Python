# a = input()
# b = int(input())
# c = int(input())
#
# d = 0
#
# if a == "Roses":
#     d=b*5
#     if b>80:
#         d-=d*0.1
# elif a == "Dahlias":
#     d=b*3.8
#     if b>90:
#         d-=d*0.15
# elif a == "Tulips":
#     d=b*2.8
#     if b>80:
#         d-=d*0.15
# elif a == "Narcissus":
#     d=b*3
#     if b<120:
#         d+=d*0.15
# elif a == "Gladiolus":
#     d=b*2.5
#     if b<80:
#         d+=d*0.2
#
# if c>=d:
#     print(f"Hey, you have a great garden with {b} {a} and {c-d:.2f} leva left.")
# else:
#     print(f"Not enough money, you need {d-c:.2f} leva more.")

# User Input
type_flowers = input()  # "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
flowers_count = int(input())
budget = int(input())

# Logic
total_cost = 0
if type_flowers == "Roses":
    total_cost = flowers_count * 5
    if flowers_count > 80:
        total_cost -= total_cost * 0.1
elif type_flowers == "Dahlias":
    total_cost = flowers_count * 3.80
    if flowers_count > 90:
        total_cost -= total_cost * 0.15
elif type_flowers == "Tulips":
    total_cost = flowers_count * 2.80
    if total_cost > 80:
        total_cost -= total_cost * 0.15
elif type_flowers == "Narcissus":
    total_cost = flowers_count * 3
    if flowers_count < 120:
        total_cost += total_cost * 0.15
elif type_flowers == "Gladiolus":
    total_cost = flowers_count * 2.50
    if flowers_count < 80:
        total_cost += total_cost * 0.20

# Print Output
if budget >= total_cost:
    print(f'Hey, you have a great garden with {flowers_count} {type_flowers} and {budget - total_cost:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_cost - budget:.2f} leva more.')