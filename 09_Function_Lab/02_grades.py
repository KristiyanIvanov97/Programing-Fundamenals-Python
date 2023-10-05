def grade_as_string(some_grade):
    if 2 <= some_grade <= 2.99:
        print("Fail")
    elif 3.00 <= some_grade <= 3.49:
        print("Poor")
    elif 3.50 <= some_grade <= 4.49:
        print("Good")
    elif 4.50 <= some_grade <= 5.49:
        print("Very Good")
    elif 5.50 <= some_grade <= 6.00:
        print("Excellent")


grade = float(input())
grade_as_string(grade)
