import re

pattern = r"(%(?P<customers>[A-Z][a-z]+)%[^|$%.]*<(?P<orders>\w+)>" \
          r"[^|$%.]*\|(?P<quantities>\d+)\|[^|$%.\d]*(?P<prices>\d+(\.\d+)?)\$$)"

total_income = 0

while True:
    line = input()
    if line == "end of shift":
        break

    match = re.findall(pattern, line)
    if not match:
        continue
    matches = match[0]

    customer = matches[1]
    order_is = matches[2]
    quantity_is = int(matches[3])
    price_is = float(matches[4])

    total_price = quantity_is * price_is

    print(f"{customer}: {order_is} - {total_price:.2f}")

    total_income += total_price

print(f"Total income: {total_income:.2f}")
