def check_space(some_space, cloth_space):
    if some_space - cloth_space >= 0:
        return True
    return False


stack = [int(x) for x in input().split(" ")]
capacity = int(input())

racks = 1
space = capacity
while stack:
    cloth = stack.pop()
    if check_space(space, cloth):
        space -= cloth
    else:
        stack.append(cloth)
        racks += 1
        space = capacity

print(racks)
