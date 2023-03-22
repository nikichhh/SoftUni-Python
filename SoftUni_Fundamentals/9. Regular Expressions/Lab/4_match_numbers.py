import re

text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

result = re.finditer(pattern, text)

for res in result:
    print(res.group(), end=" ")
