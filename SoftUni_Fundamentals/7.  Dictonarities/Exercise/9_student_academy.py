#def get_average_grades(grades):
    #return sum(grades) / len(grades)

n = int(input())

grades_by_student = {}

for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in grades_by_student:
        grades_by_student[student_name] = [student_grade]
    else:
        grades_by_student[student_name].append(student_grade)

for student, grades in grades_by_student.items():
    average_grade = sum(grades) / len(grades)
    if average_grade < 4.5:
        continue
    print(f"{student} -> {average_grade:.2f}")

#average_grade_by_student = {student: get_average_grade(grades) for student, grades in grades_by_student.items() if get_average_grade(grades) >= 4.5}
#for student, grade in average_grade_by_student.items():
    #print(f"{astudent} -> {gradee:.2f}")