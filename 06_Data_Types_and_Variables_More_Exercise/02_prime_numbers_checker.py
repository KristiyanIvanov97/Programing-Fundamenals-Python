number = int(input())

if number > 1:
    for divisor in range(2, number):
        if number % divisor == 0:
            print("False")
            break
    else:
        print("True")
else:
    print("False")
