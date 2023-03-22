a = int(input())
b = int(input())

last_devidable = 0

for i in range (b+1):
    if i % a == 0 and i >= a and i > 0:
        last_devidable = i

print(last_devidable)