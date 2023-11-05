students = {}

some_string = input()
while ":" in some_string:
    curr_student = some_string.split(":")
    student_name = curr_student[0]
    student_id = curr_student[1]
    course = curr_student[2]
    if course not in students.keys():
        students[course] = {}
    students[course][student_name] = student_id
    some_string = input()

searched_course = " ".join(some_string.split("_"))
for course, student in students.items():
    if course == searched_course:
        for name, id in student.items():
            print(f"{name} - {id}")


