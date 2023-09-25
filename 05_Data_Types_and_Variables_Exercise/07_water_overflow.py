number_of_lines = int(input())

capacity = 255
total_filled = 0
for i in range(number_of_lines):
    current_line = int(input())
    if current_line > capacity:
        print("Insufficient capacity!")
        continue
    capacity -= current_line
    total_filled += current_line

print(total_filled)

