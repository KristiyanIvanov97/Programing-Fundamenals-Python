numbers_as_string = input().split()
numbers_as_integers = []

for number in numbers_as_string:
    numbers_as_integers.append(round(float(number)))

print(numbers_as_integers)
