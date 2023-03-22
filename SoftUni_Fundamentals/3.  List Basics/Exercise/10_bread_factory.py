events = input().split("|")

initial_energy = 100
initial_coins = 100

for event in events:
    args = event.split("-")
    thing = args[0]
    points = int(args[1])

    if thing == "order":
        if initial_energy < 30:
            print("You had to rest!")
            initial_energy += 50
        else:
            print(f"You earned {points} coins.")
            initial_coins += points
            initial_energy -= 30
    elif thing == "rest":
        if points + initial_energy > 100:
            print(f"You gained {100 - initial_energy} energy.")
            initial_energy = 100
        else:
            initial_energy += points
            print(f"You gained {points} energy.")
        print(f"Current energy: {initial_energy}.")
    else:
        if initial_coins >= points:
            print(f"You bought {thing}.")
            initial_coins -= points
        else:
            print(f"Closed! Cannot afford {thing}.")
            exit()

print("Day completed!")
print(f"Coins: {initial_coins}\n"
      f"Energy: {initial_energy}")