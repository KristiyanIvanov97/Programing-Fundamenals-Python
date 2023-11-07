courses = {}

while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for course, student_name in courses.items():
    print(f"{course}: {len(courses[course])}")
    for student in student_name:
        print(f"-- {student}")

