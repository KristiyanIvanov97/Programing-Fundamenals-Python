number_of_electrons = int(input())
final_list_of_electrons = []
for shell in range(1, number_of_electrons + 1):
    total_electrons_in_current_shell = 2 * shell ** 2
    if number_of_electrons >= total_electrons_in_current_shell:
        final_list_of_electrons.append(total_electrons_in_current_shell)
        number_of_electrons -= total_electrons_in_current_shell
        if number_of_electrons == 0:
            break
    else:
        final_list_of_electrons.append(number_of_electrons)
        break
print(final_list_of_electrons)


