energy = 100
coins = 100
events = input().split("|")
successful_day = True

for current_event in events:
    command, number = current_event.split("-")
    number = int(number)
    if command == "rest":
        current_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            successful_day = False
            break

if successful_day:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
