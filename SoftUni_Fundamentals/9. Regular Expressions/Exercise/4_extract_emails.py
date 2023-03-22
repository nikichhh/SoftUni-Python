import re

text = input()

matches = re.findall(r"\s([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)", text)

print("\n".join(group[0] for group in matches))
