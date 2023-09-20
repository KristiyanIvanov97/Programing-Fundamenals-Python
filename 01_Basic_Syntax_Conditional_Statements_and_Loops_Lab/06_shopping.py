budget = int(input())
total_bill = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    command = float(command)
    total_bill += command

    if total_bill > budget:
        print("You went in overdraft!")
        break

