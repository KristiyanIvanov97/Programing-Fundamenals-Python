def order(some_product, quantity_of_product):
    total_price = 0
    if some_product == "coffee":
        total_price = 1.50 * quantity_of_product
    elif some_product == "water":
        total_price = 1.00 * quantity_of_product
    elif some_product == "snacks":
        total_price = 2.00 * quantity_of_product
    elif some_product == "coke":
        total_price = 1.40 * quantity_of_product
    return total_price


product = input()
quantity = int(input())

print(f"{order(product, quantity):.2f}")


