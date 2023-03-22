# man = int(input())
# female = int(input())
# tables = int(input())
#
# for i in range (1, man + 1):
#     for j in range (1, female + 1):
#         tables -= 1
#         if tables < 0:
#             exit()
#         print(f"({i} <-> {j})", end= " ")

men = int(input())
women = int(input())
tables = int(input())

counter_couples = 0

for i in range(1, men + 1):
    for j in range(1, women + 1):
        counter_couples = counter_couples + 1
        print(f"({i} <-> {j})", end=" ")
        if counter_couples >= tables:
            break
    if counter_couples >= tables:
        break