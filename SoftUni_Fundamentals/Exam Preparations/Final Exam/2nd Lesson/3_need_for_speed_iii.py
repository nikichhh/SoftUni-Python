cars_count = int(input())

fuel_by_car = {}
mileage_by_car = {}

for i in range(cars_count):
    car_args = input().split('|')
    car = car_args[0]
    mileage = int(car_args[1])
    fuel = int(car_args[2])

    fuel_by_car[car] = fuel
    mileage_by_car[car] = mileage

while True:
    line = input()
    if line == "Stop":
        break

    args = line.split(" : ")
    command = args[0]
    car = args[1]

    if command == "Drive":
        distance = int(args[2])
        fuel = int(args[3])

        if fuel_by_car[car] - fuel < 0:
            print("Not enough fuel to make that ride")
        else:
            mileage_by_car[car] += distance
            fuel_by_car[car] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if mileage_by_car[car] >= 100000:
                print(f"Time to sell the {car}!")
                fuel_by_car.pop(car)
                mileage_by_car.pop(car)

    elif command == "Refuel":
        fuel = int(args[2])

        if fuel + fuel_by_car[car] > 75:
            fuel = 75 - fuel_by_car[car]

        fuel_by_car[car] += fuel
        print(f"{car} refueled with {fuel} liters")

    else:
        kilometers = int(args[2])

        mileage_by_car[car] -= kilometers

        if mileage_by_car[car] < 10000:
            mileage_by_car[car] = 10000
            continue

        print(f"{car} mileage decreased by {kilometers} kilometers")

for car, mileage in mileage_by_car.items():
    fuel = fuel_by_car[car]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
