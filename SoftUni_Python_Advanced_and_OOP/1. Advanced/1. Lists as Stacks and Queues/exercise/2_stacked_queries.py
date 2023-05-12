def check_len_stack(some_stack):
    if some_stack:
        return True
    return False


n = int(input())
stack = []

map_functions = {
    1: lambda x: stack.append(x[1]),  # x == number_data
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None
}

for i in range(n):
    nums = [int(el) for el in input().split()]
    # operation = int(nums[0])
    map_functions[nums[0]](nums)
    #
    # if operation == 1:
    #     new_nums = int(nums[1])
    #     stack.append(new_nums)
    # elif check_len_stack(stack):
    #     if operation == 2:
    #         stack.pop()
    #     elif operation == 3:
    #         print(max(stack))
    #     else:
    #         print(min(stack))

while stack:
    el = stack.pop()
    if check_len_stack(stack):
        print(el, end=", ")
    else:
        print(el, end="")
