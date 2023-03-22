n1 = int(input())
n2 = int(input())
char = str(input())

a = 0
is_odd = ""

if char == "+" or char == "-" or char == "*":
    if char == "+":
        a = n1+n2
    elif char == "-":
        a = n1-n2
    elif char == "*":
        a = n1*n2
    if a%2 == 0:
        is_odd = "even"
    else:
        is_odd = "odd"
    print(f"{n1} {char} {n2} = {a} - {is_odd}")
elif char == "/" or char == "%":
    if n2==0:
        print(f"Cannot divide {n1} by zero")
    elif char == "/":
        a = n1/n2
        print(f"{n1} / {n2} = {a:.2f}")
    elif char == "%":
        a = n1 % n2
        print(f"{n1} % {n2} = {a}")