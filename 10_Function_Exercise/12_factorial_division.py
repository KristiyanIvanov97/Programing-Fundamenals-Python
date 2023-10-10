def calculate(number):
    for current_number in range(1, number):
        number *= current_number

    return number


first_number = int(input())
second_number = int(input())
final_number_factorial = calculate(first_number)
second_number_factorial = calculate(second_number)
final_result = final_number_factorial / second_number_factorial
print(f"{final_result:.2f}")

