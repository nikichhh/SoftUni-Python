# def password_checker(password):
#     first_valid = False
#     count_bad_chars = 0
#     sec_valid = False
#     count = 0
#     third_valid = False
#     if 6 <= len(password) <= 10:
#         first_valid = True
#     else:
#         print(f"Password must be between 6 and 10 characters")
#     for i in range(len(password)):
#         if 48 <= ord(password[i]) <= 57 or 65 <= ord(password[i]) <= 90 or 97 <= ord(password[i]) <= 122:
#             sec_valid = True
#         else:
#             count_bad_chars += 1
#     if count_bad_chars > 0:
#         sec_valid = False
#         print(f"Password must consist only of letters and digits")
#     for i in range(len(password)):
#         if 48 <= ord(password[i]) <= 57:
#             count += 1
#     if count >= 2:
#         third_valid = True
#     else:
#         print(f"Password must have at least 2 digits")
#
#     if first_valid and sec_valid and third_valid:
#         print(f"Password is valid")
#
#
# passwords = input()
# password = []
# for i in passwords:
#     password.append(i)
# password_checker

def is_valid_lenght(password):
    return 6 <= len(password) <= 10


def contains_alpha_numeric(password):
    return password.isalnum()


def contains_at_least_two_digits(password):
    count = 0
    for ch in password:
        if ch.isdigit():
            count += 1
    return count >= 2


input_password = input()

is_valid = True

if not is_valid_lenght(input_password):
    is_valid = False
    print(f"Password must be between 6 and 10 characters")

if not contains_alpha_numeric(input_password):
    is_valid = False
    print(f"Password must consist only of letters and digits")

if not contains_at_least_two_digits(input_password):
    is_valid = False
    print(f"Password must have at least 2 digits")

if is_valid:
    print(f"Password is valid")