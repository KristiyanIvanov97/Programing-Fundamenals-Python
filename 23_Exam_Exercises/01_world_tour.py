stops = input()
command = input()

while command != "Travel":
    if command.startswith("Add Stop:"):
        _, index, string = command.split(":")
        index = int(index)
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
    elif command.startswith("Remove Stop:"):
        _, start_index, stop_index = command.split(":")
        start_index = int(start_index)
        stop_index = int(stop_index)
        if start_index in range(len(stops)) and stop_index in range(len(stops)):
            stops = stops[:start_index] + stops[stop_index + 1:]
    elif command.startswith("Switch:"):
        _, old_string, new_string = command.split(":")
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
