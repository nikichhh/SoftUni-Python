def solve(operation, a):
    if operation == "int":
        print(int(a) * 2)
    elif operation == "real":
        print(f"{float(a) * 1.5:.2f}")
    elif operation == "string":
        print(f"${a}$")


operations = input()
n = input()

solve(operations, n)