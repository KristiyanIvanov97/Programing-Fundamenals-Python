employees_happiness = list(map(int, input().split()))
factor = int(input())

improved_happiness = list(map(lambda x: x * factor, employees_happiness))
average_happiness = sum(improved_happiness) / len(improved_happiness)
happy_count = sum(happiness >= average_happiness for happiness in improved_happiness)

if happy_count >= len(improved_happiness) / 2:
    print(f"Score: {happy_count}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(improved_happiness)}. Employees are not happy!")
