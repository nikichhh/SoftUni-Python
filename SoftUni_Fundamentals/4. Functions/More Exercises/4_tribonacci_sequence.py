def tribonacci_sequence(a):
    for i in range(a):
        if len(sequence) == 0:
            sequence.append(1)
        elif len(sequence) == 1:
            sequence.append(1)
        elif len(sequence) == 2:
            sequence.append(2)
        else:
            k = sequence[-1] + sequence[-2] + sequence[-3]
            sequence.append(k)

    for l in range(len(sequence)):
        sequence_str.append(str(sequence[l]))

    return " ".join(sequence_str)


sequence = []
sequence_str = []
n = int(input())
print(tribonacci_sequence(n))