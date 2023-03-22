key = int(input())
lenght = int(input())

word = ""

for i in range(1, lenght + 1):
    letter = input()
    word += chr(ord(letter) + key)
print(word)
