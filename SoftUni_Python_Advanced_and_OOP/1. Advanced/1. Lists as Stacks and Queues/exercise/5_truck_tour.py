from collections import deque

nums_pumps = int(input())
pumps = deque()

for i in range(nums_pumps):
    pump = [int(x) for x in input().split(" ")]
    pumps.append(pump)

for j in range(nums_pumps):
    total = 0
    found = True
    for pair in pumps:
        total = total + pair[0] - pair[1]
        if total < 0:
            pumps.append(pumps.popleft())
            found = False
            break
    if found:
        print(j)
        break
