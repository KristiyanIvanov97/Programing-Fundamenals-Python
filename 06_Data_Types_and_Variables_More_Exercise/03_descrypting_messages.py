key = int(input())
number_of_lines = int(input())
message = ""
for _ in range(number_of_lines):
    letter = input()
    new_char = key + ord(letter)
    message = message + chr(new_char)

print(message)