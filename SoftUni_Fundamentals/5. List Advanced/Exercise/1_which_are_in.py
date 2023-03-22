# def is_substr(word, seq):
#    for el in seq:
#         if word in el:
#             return True
#   return False


first_list = input().split(", ")
second_list = input().split(", ")

result = []
##result = [x for x in first_list if is_substr(x, substr)]

for substr in first_list:
    for word in second_list:
        if substr in word:
            result.append(substr)
            break
#   if is_substr(substr, second_list):
#       result.append(substr)

print(result)
