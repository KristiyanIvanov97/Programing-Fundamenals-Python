number_of_commands = int(input())
students = {}
target_average_grade = 4.50
for _ in range(number_of_commands):
    student_name = input()
    grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

for student, grade in students.items():
    average_grade = sum(grade) / len(students[student])
    if average_grade >= target_average_grade:
        print(f"{student} -> {average_grade:.2f}")
