arr = [1, 2]
frst_sum = 0
mid_sum = 0
mid_list = []
list_a1 = []
counter = 0

## Първа сума
for a in range(len(arr)-1, 0, -1):
    frst_sum += arr[a]

## Междинни суми
while True:
    mid_list.append(arr[0])
    break

## Последна сума
for a1 in arr:
    list_a1.append(a1)
    if (len(list_a1) + 1) % 2 != 0:
        continue
    else:
        for l in list_a1:
            counter += l

print(counter + frst_sum + mid_sum)