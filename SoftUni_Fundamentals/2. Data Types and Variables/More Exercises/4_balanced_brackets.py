number_lines = int(input())

is_opened = False
is_balanced = True

for i in range(0, number_lines):
    putting = input()
    if putting == "(":
        if not is_opened:
            is_opened = True
        else:
            is_balanced = False

    if putting == ")":
        if is_opened:
            is_opened = False
        else:
            is_balanced = False
if is_balanced and not is_opened:
    print("BALANCED")
else:
    print("UNBALANCED")