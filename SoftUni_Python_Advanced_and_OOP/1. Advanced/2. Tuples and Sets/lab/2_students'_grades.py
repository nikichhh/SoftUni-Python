marks = int(input())

grades_by_students = {}

for i in range(marks):
    student, grade = tuple(input().split(' '))
    grade = float(grade)

    if student not in grades_by_students:
        grades_by_students[student] = []

    grades_by_students[student].append(grade)

for name, grade in grades_by_students.items():
    print(f"{name} -> {' '.join(str(f'{mark:.2f}') for mark in grade)} (avg: {sum(grade) / len(grade):.2f})")
