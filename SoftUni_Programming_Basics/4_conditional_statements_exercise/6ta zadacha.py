a = float(input())
b = float(input())
c = float(input())

time = b*c
bonus_time = (b//15)*12.5
time+=bonus_time

if time<a:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time-a:.2f} seconds slower.")