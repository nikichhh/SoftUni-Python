import re

participants = input().split(", ")
first_pattern = r"[A-Za-z]+"
racers = {}

while True:
    name = ''
    line = input()
    if line == "end of race":
        break

    name_match = re.findall(first_pattern, line)
    for letter in name_match:
        name += letter

    if name in participants:
        distances = re.findall(r"\d", line)
        distance = sum(int(d) for d in distances)

        if name in racers:
            racers[name] += distance
        else:
            racers[name] = distance

sorted_racers = sorted(racers.items(), key=lambda x: -x[1])
top_racers = [r for r in sorted_racers[:3]]
first = top_racers[0]
second = top_racers[1]
third = top_racers[2]

print(f"1st place: {first[0]}")
print(f"2nd place: {second[0]}")
print(f"3rd place: {third[0]}")
