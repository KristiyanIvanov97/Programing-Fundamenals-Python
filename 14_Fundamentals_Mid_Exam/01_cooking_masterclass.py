from math import ceil

budget = float(input())
students = int(input())
price_for_pack_of_flour = float(input())
price_for_single_egg = float(input())
price_for_single_apron = float(input())
flour = 0

for student in range(1, students + 1):
    if student % 5 != 0:
        flour += 1

apron = ceil(students * 1.20)
eggs = price_for_single_egg * 10 * students
needed_items = price_for_pack_of_flour * flour + eggs + apron * price_for_single_apron

if budget >= needed_items:
    print(f"Items purchased for {needed_items:.2f}$.")
else:
    print(f"{needed_items - budget :.2f}$ more needed.")
