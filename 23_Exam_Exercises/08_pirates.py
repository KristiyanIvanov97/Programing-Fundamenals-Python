command = input()
cities = {}
while command != "Sail":
    city, population, gold = command.split("||")
    if city not in cities:
        cities[city] = [0, 0]
    cities[city][0] += int(population)
    cities[city][1] += int(gold)
    command = input()

new_command = input()

while new_command != "End":
    if new_command.startswith("Plunder"):
        action, town, people, gold = new_command.split("=>")
        cities[town][0] -= int(people)
        cities[town][1] -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] == 0 or cities[town][1] == 0:
            print(f"{town} has been wiped off the map!")
            cities.pop(town)
    elif new_command.startswith("Prosper"):
        action, town, gold = new_command.split("=>")
        if int(gold) < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    new_command = input()

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, info in cities.items():
        print(f"{town} -> Population: {info[0]} citizens, Gold: {info[1]} kg")

