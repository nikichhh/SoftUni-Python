n, m = map(int, input().split()) # [int(x) for x in range(input().split())]

n_set, m_set = set(), set() # {int(input()) for _ in range(n)}, {{int(input()) for _ in range(m)}}

for i in range(n):
    num = int(input())
    n_set.add(num)

for j in range(m):
    num = int(input())
    m_set.add(num)


print(*n_set.intersection(m_set), sep='\n')
# while n_set and m_set:
#     if len(n_set) >= len(m_set):
#         num = n_set.pop()
#         if num in m_set:
#             print(num)
#     else:
#         num = m_set.pop()
#         if num in n_set:
#             print(num)
