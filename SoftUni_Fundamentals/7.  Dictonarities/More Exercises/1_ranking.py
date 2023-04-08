courses = {}

while True:
    course = input()
    if course == 'end of contests':
        break
    line = course.split(":")

    courses[line[0]] = line[1]

submissions = {}
total_points = {}
while True:
    submission = input()
    if submission == "end of submissions":
        break
    line = submission.split("=>")
    contest = line[0]
    password = line[1]
    user = line[2]
    points = int(line[3])

    if contest in courses:
        if password == courses[contest]:
            if user in submissions:
                if contest not in submissions[user]:
                    submissions[user][contest] = points
                    total_points[user] += points
                else:
                    if points > submissions[user][contest]:
                        submissions[user][contest] = points
                        total_points[user] += points
            else:
                submissions[user] = {contest: points}
                total_points[user] = points

max_score = max(total_points.values())
needed_person = ''
for key, value in total_points.items():
    if value == max_score:
        needed_person = key
        break

print(f"Best candidate is {needed_person} with total {max_score} points.\nRanking:")

for person, final_score in sorted(submissions.items()):
    print(person)
    for course_name, course_points in sorted(final_score.items(), key=lambda kv: kv[1], reverse=True):
        print(f"#  {course_name} -> {course_points}")
