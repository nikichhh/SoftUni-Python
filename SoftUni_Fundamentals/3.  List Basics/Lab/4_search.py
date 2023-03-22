n = int(input())
word = input()

all_list = []

for i in range(1, n + 1):
    string = input()
    all_list.append(string)
print(all_list)

for k in range(len(all_list) -1, -1, -1):
    element = all_list[k]
    if word not in element:
        all_list.remove(element)
print(all_list)
