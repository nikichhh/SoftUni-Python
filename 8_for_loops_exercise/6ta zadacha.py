name = input()
points = float(input())
jury_cnt = int(input())

for i in range(1,jury_cnt+1):
    jury_name = input()
    gvn_points = float(input())
    lenght_jury_name = len(jury_name)
    cur_score = (lenght_jury_name*gvn_points)/2
    points+=cur_score
    if points>=1250.5:
        break

if points>=1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {name} you need {(1250.5-points):.1f} more!")