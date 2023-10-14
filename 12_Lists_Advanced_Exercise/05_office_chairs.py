number_of_rooms = int(input())
free_chairs = 0
needed_chairs = []
for current_room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()
    if len(chairs_and_visitors[0]) >= int(chairs_and_visitors[1]):
        free_chairs += (len(chairs_and_visitors[0]) - int(chairs_and_visitors[1]))
    else:
        needed_chairs_in_room = int(chairs_and_visitors[1]) - len(chairs_and_visitors[0])
        message_for_need = f"{needed_chairs_in_room} more chairs needed in room {current_room}"
        needed_chairs.append(message_for_need)

if len(needed_chairs) >= 1:
    print("\n".join(needed_chairs))
else:
    print(f"Game On, {free_chairs} free chairs left")
