some_list = input().split()
some_list_as_integers = []
for current_int in some_list:
    some_list_as_integers.append(int(current_int))

final_list = list(filter(lambda x: x % 2 == 0, some_list_as_integers))
print(final_list)
