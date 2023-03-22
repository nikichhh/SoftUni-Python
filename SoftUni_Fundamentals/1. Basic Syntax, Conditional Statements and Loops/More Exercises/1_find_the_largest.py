num = input()

list = []

for i in (num):
    list.append(int(i))

while 0 < len(list):
    max_index = (max(list))
    print(max_index, end = '')
    list.remove(max(list))