negative_numbers = []


def positive_or_negative(a, b, c):
    result = None
    if a < 0:
        negative_numbers.append(a)
    if b < 0:
        negative_numbers.append(b)
    if c < 0:
        negative_numbers.append(c)
    if a == 0 or b == 0 or c == 0:
        result = "zero"
    elif len(negative_numbers) == 1 or len(negative_numbers) == 3:
        result = "negative"
    else:
        result = "positive"
    return result


m = int(input())
n = int(input())
p = int(input())

print(positive_or_negative(m, n, p))