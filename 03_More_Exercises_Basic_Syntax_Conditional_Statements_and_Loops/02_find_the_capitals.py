string = input()

capital_letters_indices = []

for i in range(len(string)):
    if string[i].isupper():
        capital_letters_indices.append(i)

print(capital_letters_indices)