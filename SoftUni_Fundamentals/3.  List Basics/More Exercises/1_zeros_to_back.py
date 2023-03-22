from sys import maxsize
string = input()

int_list = string.split(", ")

for k in range(0, len(int_list)):
    int_list[k] = int(int_list[k])

for i in range(len(int_list) - 1, -1, -1):
    element = int_list[i]
    if element == 0:
        int_list.insert(maxsize, int_list.pop(int_list.index(element)))

print(int_list)
