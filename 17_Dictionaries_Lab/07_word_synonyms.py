number_of_words = int(input())
synonyms = {}
for _ in range(number_of_words):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for curr_word, synonym in synonyms.items():
    print(f"{curr_word} - {', '.join(synonym)}")

