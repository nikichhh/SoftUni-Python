first_condition = ord(input())
second_condition = ord(input())
text = input()

sum_is = 0

for ch in text:
    if first_condition < ord(ch) < second_condition:
        sum_is += ord(ch)

print(sum_is)
