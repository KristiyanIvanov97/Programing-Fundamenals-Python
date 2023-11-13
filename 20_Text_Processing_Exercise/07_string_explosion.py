some_string = input()
final_string = ""
explosion_power = 0
for index in range(len(some_string)):
    if explosion_power > 0 and some_string[index] != ">":
        explosion_power -= 1
    elif some_string[index] == ">":
        final_string += some_string[index]
        explosion_power += int(some_string[index + 1])
    else:
        final_string += some_string[index]

print(final_string)
