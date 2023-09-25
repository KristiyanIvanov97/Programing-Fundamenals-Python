from math import floor
number_of_people = int(input())
days = int(input())
total_coins = 0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        number_of_people -= 2
    if current_day % 15 == 0:
        number_of_people += 5
    if current_day % 3 == 0:
        total_coins -= number_of_people * 3
    if current_day % 5 == 0:
        total_coins += number_of_people * 20
        if current_day % 3 == 0:
            total_coins -= number_of_people * 2
    total_coins += 50
    total_coins -= number_of_people * 2

coins_per_person = total_coins / number_of_people

print(f"{number_of_people} companions received {floor(coins_per_person)} coins each.")
