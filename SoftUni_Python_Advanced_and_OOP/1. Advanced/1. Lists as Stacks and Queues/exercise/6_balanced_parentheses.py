expression = input()
dictionary = {
    "{": "}",
    "[": "]",
    "(": ")"
}
stack = []
found = False

for el in expression:
    if el in "{[(":
        stack.append(el)
    else:
        if stack:
            pop_el = stack.pop()
            if not dictionary[pop_el] == el:
                found = True
                break
        else:
            found = True
            break

if stack or found:
    print("NO")
else:
    print("YES")
