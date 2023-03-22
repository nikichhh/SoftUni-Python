first_letter = input()
last_letter = input()
missed_letter = input()

combinations = 0

for i in range (ord(first_letter), ord(last_letter) + 1):

    for m in range (ord(first_letter), ord(last_letter) + 1):

        for n in range (ord(first_letter), ord(last_letter) + 1):

            if chr(i) != missed_letter and chr(m) != missed_letter and chr(n) != missed_letter:
                print(f"{chr(i)}{chr(m)}{chr(n)}", end=" ")
                combinations += 1

print(f"{combinations} ")