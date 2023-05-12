n = int(input())

chemicals = set()
for _ in range(n):
    chemical = input().split()
    for x in chemical:
        chemicals.add(x)

print(*chemicals, sep="\n")

# print(*{x for x in input().split() for _ in range(int(input()))}, sep="\n") idk how to do it

# another way to write interception - with &
# another way to write union - with |
# another way to write difference - with -
# another way to write symmetrical diff - with ^
