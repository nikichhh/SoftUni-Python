def check_index(checking, indexing):
    if 0 <= indexing < len(checking):
        return True
    return False


friends = [x for x in input().split(", ")]

blacklist_cnt = 0
lost_cnt = 0

while True:
    lists = input()
    if lists == "Report":
        break

    command = lists.split()[0]
    index = lists.split()[1]

    if command == "Blacklist":
        if index in friends:
            print(f"{index} was blacklisted.")
            friends = [x.replace(index, "Blacklisted") for x in friends]
            blacklist_cnt += 1
        else:
            print(f"{index} was not found.")

    elif command == "Error":
        if check_index(friends, int(index)) and\
            friends[int(index)] != "Blacklisted"\
                and friends[int(index)] != "Lost":
            print(f"{friends[int(index)]} was lost due to an error.")
            friends = [x.replace(friends[int(index)], "Lost") for x in friends]
            lost_cnt += 1

    elif command == "Change":
        new_name = lists.split()[2]
        if check_index(friends, int(index)):
            print(f"{friends[int(index)]} changed his username to {new_name}.")
            friends = [x.replace(friends[int(index)], new_name) for x in friends]

print(f"Blacklisted names: {blacklist_cnt}")
print(f"Lost names: {lost_cnt}")
print(" ".join(friends))