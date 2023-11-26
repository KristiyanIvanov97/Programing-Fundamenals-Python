number_of_operations = int(input())
discovered_plants = {}
for operation in range(number_of_operations):
    plant, rarity = input().split("<->")
    if plant not in discovered_plants:
        discovered_plants[plant] = {"rarity": 0, "rating": []}
    discovered_plants[plant]["rarity"] = rarity

command = input()
while command != "Exhibition":
    action, information = command.split(": ")
    plant = information.split(" - ")[0]
    if plant not in discovered_plants:
        print("error")
        command = input()
        continue
    if action == "Rate":
        rating = int(information.split(" - ")[1])
        discovered_plants[plant]["rating"].append(rating)
    elif action == "Update":
        new_rarity = int(information.split(" - ")[1])
        discovered_plants[plant]["rarity"] = new_rarity
    elif action == "Reset":
        plant = str(information)
        discovered_plants[plant]["rating"] = []
    command = input()

print("Plants for the exhibition:")
for plant, plant_information in discovered_plants.items():
    if len(plant_information["rating"]) > 0:
        average_rating = sum(plant_information["rating"]) / len(plant_information["rating"])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {discovered_plants[plant]['rarity']}; Rating: {average_rating:.2f} ")
