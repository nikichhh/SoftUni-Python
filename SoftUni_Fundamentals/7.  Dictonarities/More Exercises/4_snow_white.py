def better_physic(physic, name, colour, dictionary):
    if physic > dictionary[colour][name]:
        dictionary[colour][name] = physic
        return dictionary
    return dictionary


dwarfs_by_dict = {}
dwarfs_list = []

while True:
    line = input()
    if line == "Once upon a time":
        break

    args = line.split(" <:> ")
    name = args[0]
    colour = args[1]
    physic = int(args[2])

    if colour not in dwarfs_by_dict:
        dwarfs_by_dict[colour] = {name: physic}
    else:
        if name in dwarfs_by_dict[colour]:
            better_physic(physic, name, colour, dwarfs_by_dict)
        else:
            dwarfs_by_dict[colour][name] = physic

for colour in dwarfs_by_dict.keys():
    for name, physics_dwarf in dwarfs_by_dict[colour].items():
        dwarfs_list.append({"length": len(dwarfs_by_dict[colour]), "hat_colour": colour, "dwarf name": name,  "dwarf physics": physics_dwarf})

for final in sorted(dwarfs_list, key=lambda x: (-x["dwarf physics"], -x["length"])):
    print(f"({final['hat_colour']}) {final['dwarf name']} <-> {final['dwarf physics']}")
