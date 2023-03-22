words = input().split()

result = [word for word in words if len(word) % 2 == 0]
# for word in words:
#     if len(word) % 2 == 0:
#         result.append(word)

print("\n".join(result))

# result = list(filter(lambda x: len(x) % 2 == 0, words))
