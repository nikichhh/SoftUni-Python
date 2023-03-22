def solve(order, quantity):
    if order == "coffee":
        print(f"{quantity * 1.5:.2f}")
    elif order == "water":
        print(f"{quantity * 1.00:.2f}")
    elif order == "coke":
        print(f"{quantity * 1.4:.2f}")
    elif order == "snacks":
        print(f"{quantity * 2.00:.2f}")


order_input = input()
n = int(input())

solve(order_input, n)
