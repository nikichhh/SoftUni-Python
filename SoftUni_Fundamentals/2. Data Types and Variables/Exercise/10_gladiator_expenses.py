loses = int(input())    #all losses
helmet = float(input()) #price of helmet
sword = float(input())  #price of sword
shield = float(input()) #price of shield
armor = float(input())  #price of armor

shield_broken = 0 #starting the count of broken equipment, just to have it for later
sword_broken = 0
helmet_broken = 0
armor_broken = 0
for games in range(1, loses + 1):   #starting the logic
    if games % 2 == 0:
        helmet_broken += 1
    if games % 3 == 0:
        sword_broken += 1
    if games % 6 == 0:
        shield_broken += 1
    if games % 12 == 0:
        armor_broken += 1
#the end of logic

#doing the math work
helmet_price = helmet * helmet_broken
sword_price = sword * sword_broken
shield_price = shield * shield_broken
armor_price = armor * armor_broken
expenses = helmet_price + sword_price + shield_price + armor_price

#print the output
print(f"Gladiator expenses: {expenses:.2f} aureus")
