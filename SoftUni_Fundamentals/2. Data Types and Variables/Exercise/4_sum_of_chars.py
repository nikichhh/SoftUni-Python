n = int(input())

sum = 0

for i in range(1, n+1):
    a = input()
    sum += ord(a)
print(f"The sum equals: {sum}")
