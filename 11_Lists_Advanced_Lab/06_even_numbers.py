list_of_numbers = list(map(int, input().split(", ")))

new_list = [curr_number for curr_number in range(len(list_of_numbers)) if list_of_numbers[curr_number] % 2 == 0]

print(new_list)
