text = input().split()


def swap(c, i, j):
    c = list(c)
    x = c[i]
    c[i], c[j] = c[j], x
    return "".join(c)


res = []

for key in text:
    list_zero = [i for i in key if i.isdigit()]
    list_element = [j for j in key if not j.isdigit()]
    num = chr(int("".join(list_zero)))
    list_element.insert(0, num)
    res.append(swap(list_element, 1, - 1))
    res.append(" ")
    list_zero.clear()
    list_element.clear()

res = "".join(res)

print(res)
