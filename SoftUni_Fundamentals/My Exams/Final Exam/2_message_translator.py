import re

pattern = r'!([A-Z][a-z]+)!:\[([A-Za-z\s]+)\]'

n = int(input())

name = ''
new_message = ''
for i in range(n):
    message = input()

    decryption = re.findall(pattern, message)
    if not decryption:
        print('The message is invalid')
    else:
        encrypt = decryption[0]
        name = encrypt[0]
        new_message = list(encrypt[1])

        for ch in range(len(new_message)):
            new_message[ch] = str(ord(new_message[ch]))

        print(f"{name}: {' '.join(new_message)}")
