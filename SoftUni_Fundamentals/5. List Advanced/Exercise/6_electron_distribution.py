electrons = int(input())
result = []

while electrons > 0:
    n = len(result) + 1
    shell_value = 2 * (n ** 2)
    if shell_value > electrons:
        result.append(electrons)
        break
    else:
        result.append(shell_value)
    electrons -= shell_value

print(result)