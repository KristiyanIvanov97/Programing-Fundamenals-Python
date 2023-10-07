some_numbers = input().split()
numbers_as_integers = []
for current_number in some_numbers:
    numbers_as_integers.append(int(current_number))


print(sorted(numbers_as_integers))
