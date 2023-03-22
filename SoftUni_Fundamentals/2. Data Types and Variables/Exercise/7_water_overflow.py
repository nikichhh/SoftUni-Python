n = int(input())

capacity = 255

for i in range(0, n):
    water = int(input())
    if capacity - water < 0:
        print("Insufficient capacity!")
        continue
    capacity -= water
print(f"{255-capacity}")