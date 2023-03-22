x, y, z = [int(x) for x in input().split(".")]

z += 1

if z == 10:
    z = 0
    y += 1
    if y == 10:
        y = 0
        x += 1

print(f"{x}.{y}.{z}")

# version = "".join(input().split("."))
# new_version = int(version) + 1
# print(".".join(str(new_version)))