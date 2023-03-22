phones_storage = [x for x in input().split(", ")]

while True:
    lists = input()
    if lists == "End":
        break

    command = lists.split(" - ")[0]
    phones = lists.split(" - ")[1]

    if command == "Add":
        if phones not in phones_storage:
            phones_storage.append(phones)

    elif command == "Remove":
        if phones in phones_storage:
            phones_storage.remove(phones)

    elif command == "Bonus phone":
        old_phone = phones.split(":")[0]
        new_phone = phones.split(":")[1]
        if old_phone in phones_storage:
            idx = phones_storage.index(old_phone)
            phones_storage.insert(idx + 1, new_phone)

    elif command == "Last":
        if phones in phones_storage:
            phones_storage.append(phones_storage.pop(phones_storage.index(phones)))

print(*phones_storage, sep=", ")