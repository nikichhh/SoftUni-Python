fuel = input()
tank_fuel = float(input())

if fuel == "Diesel":
    pass
elif fuel == "Gasoline":
    pass
elif fuel == "Gas":
    pass
else:
    print("Invalid fuel!")
    exit()

if tank_fuel < 25:
    print(f"Fill your tank with {fuel.lower()}!")
else:
    print(f"You have enough {fuel.lower()}.")