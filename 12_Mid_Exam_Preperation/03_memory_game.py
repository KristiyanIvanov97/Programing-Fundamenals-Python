def main():
    sequence_of_elements = input().split()
    number_of_moves = 0
    while True:
        number_of_moves += 1
        command = input().split()
        if command[0] == "end":
            print(f"Sorry you lose :(")
            print(' '.join(map(str, sequence_of_elements)))
            break

        index1 = int(command[0])
        index2 = int(command[1])
        if is_invalid_input(index1, index2, sequence_of_elements):
            invalid_indexes(index1, index2, sequence_of_elements,number_of_moves)
        else:
            valid_index(index1, index2, sequence_of_elements)
        if len(sequence_of_elements) == 0:
            print(f"You have won in {number_of_moves} turns!")
            break


def is_invalid_input(index1, index2, sequence):
    return index1 == index2 or \
            index1 < 0 or \
            index1 >= len(sequence) or \
            index2 >= len(sequence) or \
            index2 < 0


def invalid_indexes(index1, index2, sequence, moves):
        middle_index = len(sequence) // 2
        sequence.insert(middle_index, f"-{moves}a")
        sequence.insert(middle_index, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")


def valid_index(index1, index2, sequence):
    if sequence[index1] == sequence[index2]:
        curr_element = sequence[index1]
        sequence.remove(curr_element)
        sequence.remove(curr_element)
        print(f"Congrats! You have found matching elements - {curr_element}!")
    else:
        print("Try again!")


main()
