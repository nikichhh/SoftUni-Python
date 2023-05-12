from collections import deque


def check_food(quantity, the_order):
    if quantity - the_order >= 0:
        return True
    return False


def check_queue(queue):
    if queue:
        return True
    return False


quantity_of_food = int(input())
orders = [int(el) for el in input().split(" ")]
all_orders = deque(orders)

print(max(all_orders))

while all_orders:
    order = all_orders.popleft()
    if check_food(quantity_of_food, order):
        quantity_of_food -= order
    else:
        all_orders.appendleft(order)
        break

if not check_queue(all_orders):
    print("Orders complete")
else:
    print(f"Orders left: ", end="")
    while all_orders:
        order = all_orders.popleft()
        if check_queue(all_orders):
            print(order, end=" ")
        else:
            print(order, end="")
