import re

text = input()
pattern = r"\b(?P<day>\d{2})([\./-])(?P<month>[A-Z][a-z]+)\2(?P<year>\d{4})\b"

matches = re.finditer(pattern, text)

for match in matches:
    # date_data = match.groupdict()
    # print(f"Day: {date_data['day']}, Month: {date_data['month']}, Year: {date_data['year']}")
    print(f"Day: {match[1]}, Month: {match[3]}, Year: {match[4]}")
