def valid_password(password: str):
    counter = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    if len(password) < 8:
        print('Password must be at least 8 characters long!')
    for ch in password:
        if not ch.isalnum() and ch != '_':
            counter += 1
    if counter > 0:
        print('Password must consist only of letters, digits and _!')
    for ch in password:
        if ch.isupper():
            counter_2 += 1
    if counter_2 == 0:
        print('Password must consist at least one uppercase letter!')
    for ch in password:
        if ch.islower():
            counter_3 += 1
    if counter_3 == 0:
        print('Password must consist at least one lowercase letter!')
    for ch in password:
        if ch.isnumeric():
            counter_4 += 1
    if counter_4 == 0:
        print('Password must consist at least one digit!')
    return


def valid_char(char: str, password):
    if char in password:
        return True
    return False


def valid_index(index, password):
    if index < len(password):
        return True
    return False


password = input()

while True:
    new_password = input()
    if new_password == 'Complete':
        break

    new_password = new_password.split()
    command = new_password[0]

    if len(new_password) > 1:
        if len(new_password[1]) > 1 and new_password[1].isalpha():
            command = ' '.join(new_password[:2])

    if command == 'Make Upper':
        index = int(new_password[-1])
        password = password[:index] + password[index].upper() + password[index + 1:]
        print(password)
    elif command == 'Make Lower':
        index = int(new_password[-1])
        password = password[:index] + password[index].lower() + password[index + 1:]
        print(password)
    elif command == 'Insert':
        index = int(new_password[1])
        char = new_password[2]

        if valid_index(index, password):
            password = password[:index] + char + password[index:]
            print(password)
    elif command == 'Replace':
        char = new_password[1]
        value = int(new_password[2])
        new_char = chr(ord(char) + value)

        if valid_char(char, password):
            password = password.replace(char, new_char)
            print(password)
    elif command == 'Validation':
        valid_password(password)
