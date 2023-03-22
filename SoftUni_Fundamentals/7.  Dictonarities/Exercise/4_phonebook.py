phone_numbers = {}

n = 0

while True:
    line = input()
    phone = line.split("-")
    if len(phone) == 1:
        n = int(line)
        break

    name = phone[0]
    number = phone[1]
    phone_numbers[name] = number

for x in range(n):
    name = input()
    if name in phone_numbers:
        print(f"{name} -> {phone_numbers[name]}")
    else:
        print(f"Contact {name} does not exist.")
