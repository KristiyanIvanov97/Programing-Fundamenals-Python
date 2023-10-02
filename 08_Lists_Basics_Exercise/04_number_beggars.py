list_of_numbers = input().split(', ')
number_of_beggars = int(input())
money_as_string = []
beggars_money = []

for money in list_of_numbers:
    money_as_string.append(int(money))

start_index = 0
while start_index < number_of_beggars:
    current_beggar_money = 0
    for current_index in range(start_index, len(money_as_string), number_of_beggars):
        current_beggar_money += money_as_string[current_index]
    beggars_money.append(current_beggar_money)
    start_index += 1

print(beggars_money)
