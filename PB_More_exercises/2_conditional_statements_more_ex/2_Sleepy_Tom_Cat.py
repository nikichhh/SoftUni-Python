n = int(input())

minutes_played = n * 127 + (365 - n) * 63

if 30000 >= minutes_played:
    print(f"Tom sleeps well\n{(30000 - minutes_played) // 60} hours and {(30000 - minutes_played) % 60} minutes less for play")
else:
    print(f"Tom will run away\n{abs(30000 - minutes_played) // 60} hours and {abs(30000 - minutes_played) % 60} minutes more for play")