def banned(users: dict, name):
    for total_users in users.keys():
        if name in users[total_users]:
            users[total_users].pop(name)

    return users


users_by_language = {}
submissions_by_language = {}
while True:
    line = input()
    if line == 'exam finished':
        break

    command = line.split('-')
    username = command[0]
    language = command[1]

    if language == 'banned':
        users_by_language = banned(users_by_language, username)
        continue

    points = int(command[2])

    if language not in users_by_language:
        users_by_language[language] = {username: [points]}
        submissions_by_language[language] = 1
    else:
        submissions_by_language[language] += 1
        if username not in users_by_language[language]:
            users_by_language[language][username] = [points]
        else:
            users_by_language[language][username].append(points)

print("Results:")

for language in users_by_language.keys():
    for username, points in users_by_language[language].items():
        print(f"{username} | {max(points)}")

print("Submissions:")
for languages in users_by_language.keys():
    print(f"{languages} - {submissions_by_language[languages]}")
