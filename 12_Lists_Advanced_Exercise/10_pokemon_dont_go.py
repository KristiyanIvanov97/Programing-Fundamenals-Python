some_integers = [int(number) for number in input().split()]
sum_of_removed_elements = 0
while some_integers:
    index = int(input())
    if index < 0:
        some_integers[0] = some_integers[-1]
        removed_element = some_integers[-1]
    elif index >= len(some_integers):
        some_integers[-1] = some_integers[0]
        removed_element = some_integers[0]
    else:
        removed_element = some_integers.pop(index)
    sum_of_removed_elements += removed_element
    for i in range(len(some_integers)):
        if some_integers[i] <= removed_element:
            some_integers[i] += removed_element
        else:
            some_integers[i] -= removed_element

print(sum_of_removed_elements)
