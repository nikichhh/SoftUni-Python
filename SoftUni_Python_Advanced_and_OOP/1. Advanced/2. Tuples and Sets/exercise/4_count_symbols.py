# occurrence = {}
#
# for el in input():
#     occurrence[el] = occurrence[el].get(el, 0) + 1
#     if el not in occurrence:
#         occurrence[el] = 0
#
#     occurrence[el] += 1
#
# for el, times in sorted(occurrence.items()):
#     print(f"{el}: {times} time/s")

sentence = input()

for letter in sorted(set(sentence)):
    print(f"{letter}: {sentence.count(letter)} time/s")
