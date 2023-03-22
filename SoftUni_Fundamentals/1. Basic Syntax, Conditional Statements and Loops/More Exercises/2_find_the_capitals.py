word = input()
index_list = []
for i in range (len(word)):
    if word[i].isupper():
        index_list.append(i)
    else:
        continue

print(index_list)