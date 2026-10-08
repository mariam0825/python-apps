def calculate_product(*number):
    product = 1

    for value in number:

        product *= value

    return product

print(calculate_product(5, 10))
