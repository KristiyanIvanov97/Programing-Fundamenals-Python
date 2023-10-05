def calculation(operator, first_number, second_number):
    result = 0
    if operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number
    elif operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number // second_number
    return result


some_operator = input()
number_one = int(input())
number_two = int(input())

print(calculation(some_operator, number_one, number_two))
