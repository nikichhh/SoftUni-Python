n = input()

prime = 0
non_prime = 0

while n != "stop":
    curr_num = int(n)

    if curr_num < 0:
        print("Number is negative.")
        n = input()
        continue

    is_prime = True

    for i in range (2, curr_num):
        if curr_num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime += curr_num
    else:
        non_prime += curr_num

    n = input()

print(f"Sum of all prime numbers is: {prime}\nSum of all non prime numbers is: {non_prime}")