strings = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle_of_deck = len(strings) // 2
    left_side = strings[:middle_of_deck]
    right_side = strings[middle_of_deck:]
    deck_after_shuffling = []
    for card in range(len(left_side)):
        deck_after_shuffling.append(left_side[card])
        deck_after_shuffling.append(right_side[card])
    strings = deck_after_shuffling

print(deck_after_shuffling)
