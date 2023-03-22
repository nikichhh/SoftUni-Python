needed_sum = int(input())
transaction = input()

cash = 0
card = 0

avr_cash = 0
avr_card = 0
cnt = 0

while transaction != "End" and needed_sum >= 0:
    cnt += 1

    if cnt % 2 != 0:
        if int(transaction) <= 100:
            print("Product sold!")
            cash += int(transaction)
            avr_cash += 1
        else:
            print("Error in transaction!")
    else:
        if int(transaction) >= 10:
            print("Product sold!")
            card += int(transaction)
            avr_card += 1
        else:
            print("Error in transaction!")

    if cash + card >= needed_sum:
        break

    transaction = input()

if cash + card >= needed_sum:
    print(f"Average CS: {cash / avr_cash:.2f}\nAverage CC: {card / avr_card:.2f}")
else:
    print("Failed to collect required money for charity.")