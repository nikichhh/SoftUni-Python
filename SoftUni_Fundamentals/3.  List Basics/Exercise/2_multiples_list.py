addable = int(input())
lenght = int(input())

zero = 0
the_list = []

for i in range(0, lenght):
    zero += addable
    the_list.append(zero)

print(the_list)