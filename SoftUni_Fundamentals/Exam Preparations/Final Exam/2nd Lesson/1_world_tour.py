def is_valid_idx(index, seq):
    return 0 <= index < len(seq)


text = input()

while True:
    line = input()
    if line == "Travel":
        break

    args = line.split(":")
    command = args[0]

    if command == "Add Stop":
        idx = int(args[1])
        new_stop = args[2]

        if is_valid_idx(idx, text):
            text = text[:idx] + new_stop + text[idx:]
    elif command == "Remove Stop":
        start_idx = int(args[1])
        end_idx = int(args[2])

        if is_valid_idx(start_idx, text) and is_valid_idx(end_idx, text):
            text = text[:start_idx] + text[end_idx + 1:]
    else:
        old_string = args[1]
        new_string = args[2]

        text = text.replace(old_string, new_string)

    print(text)

print(f"Ready for world tour! Planned stops: {text}")