some_string = input().split(">>")
total_tax_to_pay = 0
total_tax_collected = 0
for curr_car in some_string:
    car_type, year_for_pay, km_traveled = curr_car.split()

    if car_type == "family":
        km_tax = int(km_traveled) // 3000 * 12
        total_tax_to_pay = (50 - int(year_for_pay) * 5) + km_tax
    elif car_type == "heavyDuty":
        km_tax = int(km_traveled) // 9000 * 14
        total_tax_to_pay = (80 - int(year_for_pay) * 8) + km_tax
    elif car_type == "sports":
        km_tax = int(km_traveled) // 2000 * 18
        total_tax_to_pay = (100 - int(year_for_pay) * 9) + km_tax
    else:
        print("Invalid car type.")
        continue
    total_tax_collected += total_tax_to_pay
    print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
