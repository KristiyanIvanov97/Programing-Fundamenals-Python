start_index = int(input())
final_index = int(input())

for current_char in range(start_index, final_index + 1):
    current_char = chr(current_char)
    print(current_char, end=" ")
