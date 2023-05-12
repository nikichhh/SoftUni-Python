from collections import deque

cup_capacity = deque([int(x) for x in input().split()])
bottle_capacity = deque([int(x) for x in input().split()])

wasted_water = 0

while cup_capacity and bottle_capacity:
    cup = cup_capacity.popleft()
    bottle = bottle_capacity.pop()

    while cup > 0:
        cup -= bottle
        if cup <= 0:
            wasted_water += abs(cup)
            break
        bottle = bottle_capacity.pop()

if cup_capacity:
    print(f"Cups: {' '.join(str(some_cup) for some_cup in cup_capacity)}")

if bottle_capacity:
    print(f"Bottles: {' '.join(str(some_bottle) for some_bottle in bottle_capacity)}")

print(f"Wasted litters of water: {wasted_water}")
