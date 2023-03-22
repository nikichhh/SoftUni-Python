from math import floor

turnirs = int(input())
ranglist = int(input())

final_points = ranglist
wins = 0

for i in range(0,turnirs):
    win_lose = input()
    if win_lose == "W":
        final_points+=2000
        wins+=1
    elif win_lose == "F":
        final_points+=1200
    else:
        final_points+=720

average_points = (final_points-ranglist)/turnirs

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{float(wins/turnirs*100):.2f}%")