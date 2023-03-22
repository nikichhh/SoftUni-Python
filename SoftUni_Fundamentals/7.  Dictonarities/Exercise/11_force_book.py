def line_up(up_dict: dict, side, user):
    for total_users in up_dict.values():
        if user in total_users:
            return up_dict

    if side not in up_dict:
        up_dict[side] = [user]
        return up_dict

    elif side in up_dict and user not in up_dict[side]:
        up_dict[side].append(user)
        return up_dict


def arrow(arrow_dict: dict, side, user):
    for total_sides in arrow_dict.keys():
        if user in arrow_dict[total_sides]:
            arrow_dict[total_sides].remove(user)
            arrow_dict[side].append(user)
            print(f"{user} joins the {side} side!")
            return arrow_dict

    if side not in arrow_dict:
        arrow_dict[side] = [user]

    elif side in arrow_dict and user not in arrow_dict[side]:
        arrow_dict[side].append(user)

    print(f"{user} joins the {side} side!")
    return arrow_dict


users_by_side = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if "|" in line:
        command = line.split(' | ')
        side = command[0]
        user = command[1]
        users_by_side = line_up(users_by_side, side, user)

    elif "->" in line:
        command = line.split(' -> ')
        side = command[1]
        user = command[0]
        users_by_side = arrow(users_by_side, side, user)

for side, users in users_by_side.items():
    if len(users) == 0:
        continue

    print(f"Side: {side}, Members: {len(users)}")

    for user in users:
        print(f"! {user}")
