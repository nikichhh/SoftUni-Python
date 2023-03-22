special_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}

legendary_item_by_material = {
    'shards': "Shadowmourne",
    'fragments': "Valanyr",
    'motes': "Dragonwrath"
}

junk_materials = {}

crafted = False
while not crafted:
    line = input()
    materials = line.split(" ")

    for idx in range(0, len(materials) - 1, 2):
        quantity = int(materials[idx])
        material = materials[idx + 1].lower()

        if material in special_materials:
            special_materials[material] += quantity
            if special_materials[material] >= 250:
                special_materials[material] -= 250
                print(f"{legendary_item_by_material[material]} obtained!")
                crafted = True
                break
        else:
            if material not in junk_materials:
                junk_materials[material] = quantity
            else:
                junk_materials[material] += quantity

for material, count in special_materials.items():
    print(f"{material}: {count}")

for material, count in junk_materials.items():
    print(f"{material}: {count}")
