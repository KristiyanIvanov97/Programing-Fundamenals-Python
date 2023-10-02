list_of_integers = input().split()
count_of_numbers_to_remove = int(input())
list_as_integers = []
final_list = []
for number in list_of_integers:
    list_as_integers.append(int(number))

copy_list = list_as_integers.copy()
copy_list.sort()

for current_number in range(count_of_numbers_to_remove):
    list_as_integers.remove(copy_list[current_number])

print(*list_as_integers, sep=", ")
