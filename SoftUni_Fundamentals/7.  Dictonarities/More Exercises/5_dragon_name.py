dragons_by_type = {}

n = int(input())

for i in range(n):
    dragon_type, name, damage, health, armor = [int(x) if x.isdigit() else x for x in input().split()]

    if dragon_type not in dragons_by_type:
        dragons_by_type[dragon_type] = {}
    if health == 'null':
        health = 250
    if damage == 'null':
        damage = 45
    if armor == 'null':
        armor = 10

    dragons_by_type[dragon_type][name] = (int(damage), int(health), int(armor))

averages = {}
for key in dragons_by_type.keys():
    average_damage, average_health, average_armor, count = 0, 0, 0, 0
    for value in dragons_by_type[key].values():
        average_damage += value[0]
        average_health += value[1]
        average_armor += value[2]
        count += 1
    averages[key] = (average_damage / count, average_health / count, average_armor / count)

for specie, values in averages.items():
    print(f"{specie}::({values[0]:.2f}/{values[1]:.2f}/{values[2]:.2f})")
    for name, stats in sorted(dragons_by_type[specie].items()):
        print(f"-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
