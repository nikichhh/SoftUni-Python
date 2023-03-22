rooms = input().split("|")
bitcoins = 0
MAX_HEALTH = 100
health = MAX_HEALTH

rooms_cnt = 0
is_death = False

for room in rooms:
    rooms_cnt += 1
    command, amount = room.split(" ")
    amount = int(amount)

    if command == "potion":
        if health + amount >= MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = 100
        else:
            print(f"You healed for {amount} hp.")
            health += amount
        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {amount} bitcoins.")
        bitcoins += amount
    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            is_death = True
            break

if is_death:
    print(f"Best room: {rooms_cnt}")
else:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoins}\n"
          f"Health: {health}")
