secret_message = input().split()
decrypted_message = []
for curr_word in secret_message:
    digit, let = "", ""
    for curr_char in curr_word:
        if curr_char.isdigit():
            digit += curr_char
        else:
            let += curr_char

    letter_for_digit = chr(int(digit))
    if len(let) != 1:
        new_word = f"{let[-1]}{let[1:-1]}{let[0]}"
    else:
        new_word = let
    new_word = letter_for_digit + new_word
    decrypted_message.append(new_word)

print(*decrypted_message)
