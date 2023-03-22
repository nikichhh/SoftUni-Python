jury_cnt = int(input())
presentation_name = input()

cnt_presentation = 0
average_score = 0
total_average = 0

while presentation_name != "Finish":
    average_score = 0
    for i in range (0,jury_cnt):
        note = float(input())
        average_score += note
    print(f"{presentation_name} - {average_score / jury_cnt:.2f}.")
    total_average += average_score
    cnt_presentation+=1
    presentation_name = input()

print(f"Student's final assessment is {total_average / (jury_cnt * cnt_presentation):.2f}.")