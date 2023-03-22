text = input()
forbidden_letters = ['a', 'o', 'i', 'u', 'e']
result = [char for char in text if char.lower() not in forbidden_letters]

print("".join(result))