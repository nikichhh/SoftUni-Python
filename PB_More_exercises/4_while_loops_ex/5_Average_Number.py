n = int(input())

summing = 0
cnt = 0

for i in range (n):
    num = int(input())
    summing += num
    cnt += 1

print(f"{summing / cnt:.2f}")