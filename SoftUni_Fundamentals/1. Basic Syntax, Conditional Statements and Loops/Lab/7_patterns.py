number = int(input())

for i in range (1, number + 1):
    for j in range (0, i):
        print('*', end = '')
    print()

for f in range (number - 1, 0, -1):
    for m in range (0, f):
        print('*', end = '')
    print()