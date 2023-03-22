import re

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

n = int(input())

for i in range(n):
    raw_data = input()

    if re.match(pattern, raw_data):
        digits = re.findall(r"\d", raw_data)
        if digits:
            product_group = "".join(digits)
        else:
            product_group = "00"

        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
