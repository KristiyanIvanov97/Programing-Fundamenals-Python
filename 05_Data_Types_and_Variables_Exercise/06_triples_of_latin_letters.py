number_of_letters = int(input())

for first_digit in range(0, number_of_letters):
    for second_digit in range(0, number_of_letters):
        for third_digit in range(0, number_of_letters):
            print(f"{chr(97 + first_digit)}{chr(97 + second_digit)}{chr(97 + third_digit)}")
