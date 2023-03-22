line = input()

while line != "End":

    destination = line
    needed_money = float(input())

    money = 0
    savings = ""
    while True:
        savings = input()
        if savings == "End":
            exit()

        money += float(savings)

        if money >= needed_money:
            print(f"Going to {destination}!")
            break
    line = input()