def check_index(some_list, indexing):
    if indexing < len(some_list):
        return True
    return False


def removing_front(some_list, indexing, ranges):
    for i in range(ranges):
        some_list.pop(indexing + i)
    return some_list


def removing_back(some_list, indexing, ranges):
    removing_front(some_list, indexing, ranges)
    for i in range(ranges):
        some_list.pop(indexing - i)
    return some_list


targets = [int(x) for x in input().split()]

while True:
    list = input()

    if list == "End":
        break

    command = list.split()[0]
    index, value = [int(el) for el in list.split() if el.isdigit()]

    if command == "Shoot":
        if check_index(targets, index):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if check_index(targets, index):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        if check_index(targets, index):
            if index < value:
                print("Strike missed!")
            else:
                removing_back(targets, index, value)
                targets.pop(index - value)
        else:
            print("Strike missed!")

print(*targets, sep="|")