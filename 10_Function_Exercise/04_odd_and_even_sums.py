def odd_and_even_sums(number):
    odd_sum = 0
    even_sum = 0
    for current_number in number:
        if int(current_number) % 2 == 0:
            even_sum += int(current_number)
        else:
            odd_sum += int(current_number)
    return odd_sum, even_sum


number_as_string = input()
sum_of_odd_digits, sum_of_even_digits = odd_and_even_sums(number_as_string)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
