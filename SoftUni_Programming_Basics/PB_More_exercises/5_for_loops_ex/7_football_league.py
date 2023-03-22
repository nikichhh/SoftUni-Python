stadium_capacity = int(input())
number_of_viewers = int(input())

A_viewers, B_viewers = 0, 0
V_viewers, G_viewers = 0, 0
A_perc, B_perc = 0, 0
V_perc, G_perc = 0, 0
all_viewers_perc = 0

for viewer in range(number_of_viewers):
    sector = input()

    if sector == 'A':
        A_viewers += 1
    elif sector == 'B':
        B_viewers += 1
    elif sector == 'V':
        V_viewers += 1
    elif sector == 'G':
        G_viewers += 1

A_perc = (A_viewers * 100) / number_of_viewers
B_perc = (B_viewers * 100) / number_of_viewers
V_perc = (V_viewers * 100) / number_of_viewers
G_perc = (G_viewers * 100) / number_of_viewers
all_viewers_perc = (number_of_viewers * 100) / stadium_capacity

print(f"{A_perc:.2f}%")
print(f"{B_perc:.2f}%")
print(f"{V_perc:.2f}%")
print(f"{G_perc:.2f}%")
print(f"{all_viewers_perc:.2f}%")