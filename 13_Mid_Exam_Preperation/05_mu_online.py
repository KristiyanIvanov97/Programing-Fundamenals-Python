health = 100
bitcoins = 0
some_commands = input().split("|")
is_killed = False
best_room = 0
for command in some_commands:
    best_room += 1
    action, number = command.split()
    if action == "potion":
        current_health = health
        health += int(number)
        if health > 100:
            health = 100
        amount = health - current_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += int(number)
        print(f"You found {number} bitcoins.")
    else:
        health -= int(number)
        if health > 0:
            print(f"You slayed {action}.")
        else:
            is_killed = True
            break

if is_killed:
    print(f"You died! Killed by {action}.")
    print(f"Best room: {best_room}")
else:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
