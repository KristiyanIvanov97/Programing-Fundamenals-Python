words = input().split()
palindrome_list = [word for word in words if word == word[::-1]]
palindrome = input()
palindrome_counter = 0
for curr_word in palindrome_list:
    if curr_word == palindrome:
        palindrome_counter += 1

print(palindrome_list, f"\nFound palindrome {palindrome_counter} times")
