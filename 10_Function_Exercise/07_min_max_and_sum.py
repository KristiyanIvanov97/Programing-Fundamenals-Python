def min_max_sum(numbers: list):
    min_number = min(numbers)
    max_number = max(numbers)
    sum_of_numbers = sum(numbers)
    return min_number, max_number, sum_of_numbers


some_list = input().split()
list_as_integers = []
for current_integer in some_list:
    list_as_integers.append(int(current_integer))

smallest_number, largest_number, sum_of_all_numbers = min_max_sum(list_as_integers)
print(f"The minimum number is {smallest_number}\nThe maximum number is {largest_number}\n"
      f"The sum number is: {sum_of_all_numbers}")
