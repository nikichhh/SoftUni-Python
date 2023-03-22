def round_it(a):
    result = round(a)
    return result


list = [float(x) for x in input().split()]
new_list = []

for i in list:
    new_list.append(round_it(i))

print(new_list)
