text = input()
new_text = text[0]

for char in text:
    if char == new_text[-1]:
        continue
    new_text += char

print(new_text)
