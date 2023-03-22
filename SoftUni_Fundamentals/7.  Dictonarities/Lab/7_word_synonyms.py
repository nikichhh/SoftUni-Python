n = int(input())
synonyms = {}

for i in range(n):
    first_word = input()
    second_word = input()

    if first_word not in synonyms:
        synonyms[first_word] = []

    synonyms[first_word].append(second_word)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
