group_tour = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
people = 0

for i in range (0,group_tour):
    num_in_group = int(input())
    people+=num_in_group
    if num_in_group<=5:
        p1+=num_in_group
    elif num_in_group<=12:
        p2+=num_in_group
    elif num_in_group<=25:
        p3+=num_in_group
    elif num_in_group<=40:
        p4+=num_in_group
    else:
        p5+=num_in_group

print(f"{float(p1/people*100):.2f}%\n{float(p2/people*100):.2f}%\n{float(p3/people*100):.2f}%")
print(f"{float(p4/people*100):.2f}%\n{float(p5/people*100):.2f}%")