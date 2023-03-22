text = input()
new_text = []

for char in text:
    new_text.append(chr(ord(char) + 3))

print("".join(new_text))
