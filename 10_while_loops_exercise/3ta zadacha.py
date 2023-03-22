needed_money = float(input())
owned_money = float(input())

days_cnt = 0
spending_cnt = 0

while owned_money < needed_money and spending_cnt < 5:
    command = input()
    money = float(input())
    days_cnt+=1

    if command == "save":
        owned_money += money
        spending_cnt = 0
    elif command == "spend":
        owned_money -= money
        spending_cnt += 1
        if owned_money < 0:
            owned_money = 0

if spending_cnt == 5:
    print(f"You can't save the money.\n{days_cnt}")
elif owned_money>=needed_money:
    print(f"You saved the money for {days_cnt} days.")