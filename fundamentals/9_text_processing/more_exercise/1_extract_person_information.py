num_names = int(input())

for i in range(num_names):
    text = input()
    name = text[text.index("@") + 1: text.index("|")]
    age = text[text.index("#") + 1: text.index("*")]
    print(f"{name} is {age} years old.")
