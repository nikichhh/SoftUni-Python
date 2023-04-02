test_words = {}

words_and_defin = input().split(' | ')

for words in words_and_defin:
    words = words.split(': ')
    word = words[0]
    definition = words[1]

    if word not in test_words:
        test_words[word] = [definition]
    else:
        test_words[word].append(definition)

question_words = input().split(' | ')
command = input()

if command == 'Hand Over':
    [print(key, end=' ') for key in test_words.keys()]
elif command == 'Test':
    for question in question_words:
        if question in test_words:
            print(f"{question}:")
            for answer in test_words[question]:
                print(f" -{answer}")
