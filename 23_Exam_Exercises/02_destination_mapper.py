import re

some_string = input()
travel_points = 0
pattern = r"([=/])([A-Z][a-zA-Z]{2,})(?=\1)"
destinations = []
valid_destination = re.findall(pattern, some_string)

for destination in valid_destination:
    travel_points += len(destination[1])
    destinations.append(destination[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
