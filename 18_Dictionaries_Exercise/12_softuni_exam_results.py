results = {}
submissions = {}
while True:
    command = input()
    if "-" not in command:
        break
    if "banned" in command:
        username = command.split("-")
        del results[username[0]]
    else:
        username, language, points = command.split("-")
        points = int(points)
        if username not in results.keys():
            results[username] = 0
        if points > results[username]:
            results[username] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
print("Results:")
for username, points in results.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, submissions_count in submissions.items():
    print(f"{language} - {submissions_count}")
