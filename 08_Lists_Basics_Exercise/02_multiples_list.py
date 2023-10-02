factor = int(input())
count = int(input())

list_with_numbers = []

for current_number in range(1, count + 1):
    new_number = current_number * factor
    list_with_numbers.append(new_number)

print(list_with_numbers)
