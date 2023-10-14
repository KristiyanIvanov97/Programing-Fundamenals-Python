list_of_numbers = list(map(int, input().split(", ")))

positive_numbers = [str(curr_digit) for curr_digit in list_of_numbers if curr_digit >= 0]
negative_numbers = [str(curr_digit) for curr_digit in list_of_numbers if curr_digit < 0]
even_numbers = [str(curr_digit) for curr_digit in list_of_numbers if curr_digit % 2 == 0]
odd_numbers = [str(curr_digit) for curr_digit in list_of_numbers if curr_digit % 2 != 0]

print(f"Positive: {', '.join(positive_numbers)}"
      f"\nNegative: {', '.join(negative_numbers)}"
      f"\nEven: {', '.join(even_numbers)}"
      f"\nOdd: {', '.join(odd_numbers)}")
