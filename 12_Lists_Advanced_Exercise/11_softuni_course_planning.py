initial_schedule = input().split(", ")
command = input()

while command != "course start":
    modify_command = command.split(":")
    if modify_command[0] == "Add":
        if modify_command[1] not in initial_schedule:
            initial_schedule.append(modify_command[1])
    if modify_command[0] == "Insert":
        if modify_command[1] not in initial_schedule:
            initial_schedule.insert(int(modify_command[2]), modify_command[1])
    if modify_command[0] == "Remove":
        if modify_command[1] in initial_schedule:
            initial_schedule.remove(modify_command[1])
    if modify_command[0] == "Swap":
        if modify_command[1] in initial_schedule and modify_command[2] in initial_schedule:
            first_lesson_to_swap = initial_schedule.index(modify_command[1])
            second_lesson_to_swap = initial_schedule.index(modify_command[2])
            initial_schedule[first_lesson_to_swap], initial_schedule[second_lesson_to_swap] = \
                initial_schedule[second_lesson_to_swap], initial_schedule[first_lesson_to_swap]
            if f'{modify_command[1]}-Exercise' in initial_schedule:
                initial_schedule.remove(f'{modify_command[1]}-Exercise')
                new_index = initial_schedule.index(modify_command[1])
                initial_schedule.insert(new_index + 1, f'{modify_command[1]}-Exercise')
            elif f'{modify_command[2]}-Exercise' in initial_schedule:
                initial_schedule.remove(f'{modify_command[2]}-Exercise')
                new_index = initial_schedule.index(modify_command[2])
                initial_schedule.insert(new_index + 1, f'{modify_command[2]}-Exercise')
    if modify_command[0] == "Exercise":
        if modify_command[1] not in initial_schedule:
            initial_schedule.append(modify_command[1])
            initial_schedule.append(f"{modify_command[1]}-Exercise")
        else:
            lesson_index = initial_schedule.index(modify_command[1])
            initial_schedule.insert(lesson_index + 1, modify_command[1])
    command = input()

for curr_lesson in range(1, len(initial_schedule) + 1):
    print(f"{curr_lesson}.{initial_schedule[curr_lesson - 1]}")
