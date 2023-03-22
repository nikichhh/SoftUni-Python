word = input()

points = 0

while word != "END":
    if word.islower():
        if word == "coding" or word == "dog" or word == "cat" or word == "movie":
            points += 1
    elif word.isupper():
        if word == "CODING" or word == "DOG" or word == "CAT" or word == "MOVIE":
            points += 2
    word = input()


if points <= 5:
    print(points)
else:
    print("You need extra sleep")