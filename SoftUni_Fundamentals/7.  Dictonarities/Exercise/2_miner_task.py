mineral = input()

all_minerals = {}

while mineral != 'stop':
    mineral_resource = input()
    if mineral_resource == 'stop':
        break

    if mineral not in all_minerals:
        all_minerals[mineral] = int(mineral_resource)
    else:
        all_minerals[mineral] += int(mineral_resource)

    mineral = input()

for minerals, quantity in all_minerals.items():
    print(f"{minerals} -> {quantity}")
