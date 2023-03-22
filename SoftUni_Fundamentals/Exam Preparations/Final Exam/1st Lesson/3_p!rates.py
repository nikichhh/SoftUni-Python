data = input()

cities = {}

while data != "Sail":
    splitted_data = data.split("||")
    city = splitted_data[0]
    population = int(splitted_data[1])
    golds = int(splitted_data[2])

    if city in cities:
        cities[city]["population"] += population
        cities[city]["gold"] += golds
    else:
        cities[city] = {"population": population, "gold": golds}

    data = input()

while True:
    data = input()
    if data == "End":
        break

    splitted_data = data.split("=>")
    command = splitted_data[0]
    city = splitted_data[1]

    if command == "Plunder":
        people = int(splitted_data[2])
        gold = int(splitted_data[3])
        if city in cities:
            cities[city]["population"] -= people
            cities[city]["gold"] -= gold
            print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
            if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
                print(f"{city} has been wiped off the map!")
                cities.pop(city)

    elif command == "Prosper":
        gold = int(splitted_data[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        if city in cities:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

if not cities:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, value in cities.items():
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
