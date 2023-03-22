# with "#" is another solution for the same problem

# def employment(a, b):
#     for x in range(len(a)):
#         a[x] = a[x] * b
#
#     return a
#
#
# def filtered(after_result):
#     listed = []
#     for x in after_result:
#         if x >= sum(after_result) / len(result):
#             listed.append(x)
#
#     return listed
#

employees = [int(x) for x in input().split(" ")]
happiness = int(input())

results = [x * happiness for x in employees]

# result = employment(employees, happiness)

filters = [x for x in results if x >= sum(results) / len(results)]

# filtering = filtered(result)

if len(filters) >= len(employees) / 2:
    print(f"Score: {len(filters)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filters)}/{len(employees)}. Employees are not happy!")
