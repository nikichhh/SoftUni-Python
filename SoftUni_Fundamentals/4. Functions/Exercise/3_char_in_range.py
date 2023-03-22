def chars(a, b):
    result = []
    for i in range(ord(a), ord(b)):
        result.append(chr(i + 1))

    result.pop(-1)
    print(" ".join(result))


n = input()
m = input()

chars(n, m)