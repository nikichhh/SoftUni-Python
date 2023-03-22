#This is the input
days = int(input())
players = int(input())
groups_energy = float(input())
water_one_person = float(input())
food_one_person = float(input())

#Getting food and water
water_all = days * water_one_person * players
food_all = days * food_one_person * players

#Start of for loop for getting the days
for day in range(1, days + 1):
    energy_loss = float(input())
    groups_energy -= energy_loss

    #Checking for the energy if it dropped 0 or below
    if groups_energy <= 0:
        print(f"You will run out of energy. You will be left with {food_all:.2f} food and {water_all:.2f} water.")
        exit(0)

    #Drinking water every 2nd day plus regaining some energy and lose some water
    if day % 2 == 0:
        groups_energy += (groups_energy * 0.05)
        water_all -= (0.3 * water_all)

    #Eating food every 3rd day plus regaining some energy and lose some food
    if day % 3 == 0:
        groups_energy += (groups_energy * 0.1)
        food_all -= (food_all / players)

print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")