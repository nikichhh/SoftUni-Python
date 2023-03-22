import re

text = input()

pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"

numbers = re.findall(pattern, text)

print(*numbers, sep=", ")
