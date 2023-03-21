def odd_length_sum(arr):
    add = 0
    for i in range(len(arr)):
        for j in range(i, len(arr), 2):
            add += sum(arr[i:j+1])
    return add


arr = [1, 4, 2, 3, 5]
print(odd_length_sum(arr))

# def odd_length_sum(arr):
#     sum = 0
#     l = len(arr)
#     for i in range(l):
#         for j in range(i, l, 2):
#             for k in range(i, j + 1, 1):
#                 sum += arr[k]
#     return sum
#
#
# arr = [34,58,99,345,12,3,5,8]
# print(odd_length_sum(arr))

# def odd_length_sum(self, arr):
#     sum = 0
#
#     for i in range(self):
#         for j in range(i, self, 2):
#             for k in range(i, j + 1, 1):
#                 sum += arr[k]
#
#     return sum
#
#
# arr = [1, 4, 2, 5, 3]
# l = len(arr)
# print(odd_length_sum(l, arr))
