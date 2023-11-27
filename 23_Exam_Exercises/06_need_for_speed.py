number_of_cars = int(input())
cars = {}
for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    if car not in cars:
        cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()

while command != "Stop":
    action = command.split(" : ")[0]
    car = command.split(" : ")[1]
    if action == "Drive":
        distance = int(command.split(" : ")[2])
        fuel = int(command.split(" : ")[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] > 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)
    elif action == "Refuel":
        max_fuel = 75
        fuel = int(command.split(" : ")[2])
        current_fuel = cars[car]["fuel"]
        cars[car]["fuel"] += fuel
        if cars[car]["fuel"] > max_fuel:
            cars[car]["fuel"] = max_fuel
        added_fuel = cars[car]["fuel"] - current_fuel
        print(f"{car} refueled with {added_fuel} liters")
    elif action == "Revert":
        kilometers = int(command.split(" : ")[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

for car, car_information in cars.items():
    print(f"{car} -> Mileage: {car_information['mileage']} kms, Fuel in the tank: {car_information['fuel']} lt.")


