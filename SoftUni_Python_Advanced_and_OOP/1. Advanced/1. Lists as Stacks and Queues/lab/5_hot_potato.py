from collections import deque

people = deque(input().split())
toss = int(input())

counter = 1
while len(people) > 1:
    kid = people.popleft()
    if counter == toss:
        print(f"Removed {kid}")
        counter = 1
    else:
        counter += 1
        people.append(kid)

print(f"Last is {people.popleft()}")

#2nd viriation
# from collections import deque
#
# people = deque(input().split())
# toss = int(input())
#
# while len(people) != 1:
#     people.rotate(toss)
#     removed_kid = people.popleft()
#     print(f"Removed {removed_kid}")
#
# print(f"Last is {people.popleft()}")
