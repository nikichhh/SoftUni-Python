from collections import deque

quantity = int(input())

people = deque()

while True:
    line = input()
    if line == 'Start':
        break

    people.append(line)

while True:
    command = input().split()
    if command[0] == 'End':
        break

    if len(command) > 1:
        quantity += int(command[1])
        continue

    if quantity - int(command[0]) < 0:
        print(f"{people.popleft()} must wait")
        continue

    quantity -= int(command[0])
    print(f"{people.popleft()} got water")


print(f"{quantity} liters left")
