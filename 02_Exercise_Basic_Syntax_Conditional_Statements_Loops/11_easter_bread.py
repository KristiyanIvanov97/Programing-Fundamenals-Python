budget = float(input())
price_for_flour = float(input())
price_for_eggs = 0.75 * price_for_flour
price_per_liter_milk = 1.25 * price_for_flour
number_of_loaves = 0
colored_eggs = 0

price_per_loaf = price_for_flour + price_for_eggs + 0.25 * price_per_liter_milk
loaf_count = budget / price_per_loaf
money_left = budget - (price_per_loaf * int(loaf_count))
for current_bread in range(1, int(loaf_count + 1)):
    number_of_loaves += 1
    colored_eggs += 3
    if current_bread % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f"You made {number_of_loaves} loaves of "
      f"Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")