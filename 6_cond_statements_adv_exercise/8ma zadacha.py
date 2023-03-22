hour1 = int(input())
min1 = int(input())
hour2 = int(input())
min2 = int(input())

min1_1 = hour1*60+min1
min2_1 = hour2*60+min2

if min2_1-min1_1>0:
    print("Late")
    if (min2_1-min1_1)//60==0:
        print(f"{min2_1-min1_1} minutes after the start")
    else:
        if (min2_1-min1_1)%60<10:
            print(f"{(min2_1 - min1_1) // 60}:0{(min2_1 - min1_1) % 60} hours after the start")
        else:
            print(f"{(min2_1-min1_1)//60}:{(min2_1-min1_1)%60} hours after the start")
elif 0<=min1_1-min2_1<=30:
    print("On time")
    if min1_1-min2_1>0:
        print(f"{min1_1-min2_1} minutes before the start")
else:
    print("Early")
    if (min1_1 - min2_1) // 60 == 0:
        print(f"{min1_1 - min2_1} minutes before the start")
    else:
        if (min1_1 - min2_1) % 60 < 10:
            print(f"{(min1_1 - min2_1) // 60}:0{(min1_1 - min2_1) % 60} hours before the start")
        else:
            print(f"{(min1_1 - min2_1) // 60}:{(min1_1 - min2_1) % 60} hours before the start")