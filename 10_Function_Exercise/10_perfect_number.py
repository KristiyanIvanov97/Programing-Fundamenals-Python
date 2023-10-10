def is_perfect(some_number):
    sum_of_divisors = 0
    for divisor in range(1, some_number + 1):
        if some_number % divisor == 0:
            sum_of_divisors += divisor

    if sum_of_divisors / 2 == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))
