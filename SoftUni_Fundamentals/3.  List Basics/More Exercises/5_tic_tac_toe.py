first_line = [int(j) for j in input().split()]
second_line = [int(j) for j in input().split()]
third_line = [int(j) for j in input().split()]

# rows
if first_line == [1, 1, 1] or second_line == [1, 1, 1] or third_line == [1, 1, 1]:
    print("First player won")

elif first_line == [2, 2, 2] or second_line == [2, 2, 2] or third_line == [2, 2, 2]:
    print("Second player won")

# columns
elif first_line[0] == 1 and second_line[0] == 1 and third_line[0] == 1 \
        or first_line[1] == 1 and second_line[1] == 1 and third_line[1] == 1 \
        or first_line[2] == 1 and second_line[2] == 1 and third_line[2] == 1:
    print("First player won")

elif first_line[0] == 2 and second_line[0] == 2 and third_line[0] == 2 \
        or first_line[1] == 2 and second_line[1] == 2 and third_line[1] == 2 \
        or first_line[2] == 2 and second_line[2] == 2 and third_line[2] == 2:
    print("Second player won")

# diagonals
elif first_line[0] == 1 and second_line[1] == 1 and third_line[2] == 1 \
        or first_line[2] == 1 and second_line[1] == 1 and third_line[0] == 1:
    print("First player won")

elif first_line[0] == 2 and second_line[1] == 2 and third_line[2] == 2 \
        or first_line[2] == 2 and second_line[1] == 2 and third_line[0] == 2:
    print("Second player won")

# draws are the rest of cases
else:
    print("Draw!")