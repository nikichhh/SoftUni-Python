from sys import maxsize

n = int(input())

weight, time_needed, quality = 0, 0, 0
max_value = -maxsize
max_weight = -maxsize
max_time = -maxsize
max_quality = -maxsize

for i in range(1, n + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight / time_needed) ** quality
    if value > max_value:
        max_value = value
        max_weight = weight
        max_time = time_needed
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_value:.0f} ({max_quality})")
