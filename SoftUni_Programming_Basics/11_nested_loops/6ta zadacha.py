floor_cnt = int(input())
room_cnt = int(input())

for fl in range (floor_cnt,0,-1):
    for room in range (0,room_cnt):
        if fl == floor_cnt:
            print(f"L{fl}{room}", end = " ")
        elif fl % 2 == 0:
            print(f"O{fl}{room}", end = " ")
        elif fl % 2 != 0:
            print(f"A{fl}{room}", end = " ")
    print("")