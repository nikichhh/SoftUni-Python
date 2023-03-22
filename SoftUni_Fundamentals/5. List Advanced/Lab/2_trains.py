n_wagons = int(input())
train = []

commands = input()

for i in range(n_wagons):
    train.append(0)

while commands != "End":
    split_data = commands.split()
    action = split_data[0]

    if action == "add":
        n_people = int(split_data[1])
        train[-1] += n_people
    elif action == "insert":
        index = int(split_data[1])
        n_people = int(split_data[2])
        train[index] += n_people

    elif action == "leave":
        index = int(split_data[1])
        n_people = int(split_data[2])
        train[index] -= n_people

    commands = input()

print(train)
