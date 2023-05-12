## first variant
n = int(input())

usernames = set()
for _ in range(n):
    usernames.add(input())

print(*usernames, sep="\n")

## second variant
# print(*{input() for _ in range(int(input()))}, sep="\n")
