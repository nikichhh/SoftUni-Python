keys_by_company = {}

while True:
    line = input()
    if line == 'End':
        break

    args = line.split(" -> ")
    company = args[0]
    key = args[1]

    if company not in keys_by_company:
        keys_by_company[company] = []

    if key not in keys_by_company[company]:
        keys_by_company[company].append(key)

for company, keys in keys_by_company.items():
    result = f"{company}"

    for key in keys:
        result += f"\n-- {key}"

    print(result)
