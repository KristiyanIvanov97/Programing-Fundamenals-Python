materials = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:
    taken_materials = input().split()
    for index in range(0, len(taken_materials), 2):
        material = taken_materials[index + 1].lower()
        quantity = int(taken_materials[index])
        if material not in materials:
            materials[material] = 0
        materials[material] += quantity

        if materials[material] >= 250:
            if material == "shards":
                materials[material] -= 250
                obtained = True
                print("Shadowmourne obtained!")
            elif material == "fragments":
                materials[material] -= 250
                obtained = True
                print("Valanyr obtained!")
            elif material == "motes":
                materials[material] -= 250
                obtained = True
                print("Dragonwrath obtained!")
            if obtained:
                break

for material, quantity in materials.items():
    print(f"{material}: {quantity}")
