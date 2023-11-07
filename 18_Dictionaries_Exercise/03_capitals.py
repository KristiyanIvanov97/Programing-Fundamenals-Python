country_name = input().split(", ")
capital_cities = input().split(", ")

# comprehension method
# final_dict = {country_name[index]: capital_cities[index] for index in range(len(country_name))}

final_dict = dict(zip(country_name, capital_cities))

for country, capital in final_dict.items():
    print(f"{country} -> {capital}")
