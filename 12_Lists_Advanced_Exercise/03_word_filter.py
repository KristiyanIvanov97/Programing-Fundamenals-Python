words = input().split()
some_words = [curr_word for curr_word in words if len(curr_word) % 2 == 0]

print("\n".join(some_words))

