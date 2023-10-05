numbers = input().split()
numbers_as_integers = []
for number in numbers:
    numbers_as_integers.append(abs(float(number)))

print(numbers_as_integers)

