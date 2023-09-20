number_to_str = input()

largest_num = ""
digits = []

for i in range(len(number_to_str)):
    digits.append(number_to_str[i])
digits.sort(reverse=True)

for j in range(len(digits)):
    largest_num += str(digits[j])

print(largest_num)
