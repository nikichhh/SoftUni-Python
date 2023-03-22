list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Error"]

a = int(input())

if a == 1:
    print(list[0])
elif a==2:
    print(list[1])
elif a==3:
    print(list[2])
elif a == 4:
    print(list[3])
elif a==5:
    print(list[4])
elif a == 6:
    print(list[5])
elif a==7:
    print(list[6])
else:
    print(list[-1])