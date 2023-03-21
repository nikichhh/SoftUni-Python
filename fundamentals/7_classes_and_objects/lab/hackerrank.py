# def is_real(grades):
#     grades = [x for x in grades if x >= 0]
#     return grades
#
#
# students = int(input())
#
# all_students = []
# low_grade = []
# new_student = []
#
# for student in range(1, students + 1):
#     name = input()
#     score = float(input())
#     low_grade.append(score)
#     all_students.append([name, score])
#
# low_grade = is_real(low_grade)
#
# while True:
#     if len(low_grade) >= 3:
#         low_grade.remove(max(low_grade))
#     else:
#         break
#
# if len(low_grade) >= 2:
#     low_grade.remove(min(low_grade))
#
# for person in all_students:
#     if person[1] in low_grade:
#         new_student.append(person[0])
#
# new_student = sorted(new_student)
#
# if len(new_student) == 0:
#     print(None)
#     exit(0)
#
# for i in range(len(new_student)):
#     print(new_student[i])

import sys


def find_mins(records: list):
    min_val = sys.float_info.max
    mins_indices = []
    for i,curr_score in enumerate(records):
        curr_score = records[i][1]
        if curr_score < min_val:
            mins_indices = [i]
        elif curr_score == min_val:
            mins_indices.append(i)
        min_val = curr_score if curr_score < min_val else min_val
    return list(map(lambda x: records[x], mins_indices))


if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append(list((name, score)))

    lowest_grades_records = find_mins(records)

    for r in lowest_grades_records:
        records.remove(r)

    records.sort(key=lambda x: x[0])
    second_lowest_grades_records = find_mins(records)
    for r in second_lowest_grades_records:
        print(r[0])