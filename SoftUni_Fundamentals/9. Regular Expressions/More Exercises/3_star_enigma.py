import re

dictionary = {"attacked": [], "destroyed": []}
attacked_count = 0
destroyed_count = 0
number = int(input())

pattern = r"@(?P<name>[A-Za-z]+)[^@\-\!\>\:]*:(?P<population>\d+)[^@\-\!\>\:]*!(?P<type>[A|D])![^@\-\!\>\:]*->(?P<soldiers>\d+)"

for i in range(number):
    text = input()
    counter = text.upper().count("S") + text.upper().count("T") + text.upper().count("A") + text.upper().count("R")
    text = list(text)

    for idx in range(len(text)):
        text[idx] = chr(ord(text[idx]) - counter)

    message = "".join(text)
    valid_message = re.finditer(pattern, message)
    for some_message in valid_message:
        if some_message["type"] == "A":
            attacked_count += 1
            dictionary["attacked"].append(some_message["name"])
        elif some_message["type"] == "D":
            destroyed_count += 1
            dictionary["destroyed"].append(some_message["name"])

sorted_attacked_dict = sorted(dictionary["attacked"])
print(f"Attacked planets: {attacked_count}")
[print(f"-> {attacked_planet}") for attacked_planet in sorted_attacked_dict]

sorted_destroyed_dict = sorted(dictionary["destroyed"])
print(f"Destroyed planets: {destroyed_count}")
[print(f"-> {destroyed_planet}") for destroyed_planet in sorted_destroyed_dict]
