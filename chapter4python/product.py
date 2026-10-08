def calculate_product(*digit):

    product = 1

    for value in digit:
        
        product  *= value
    return product

print(calculate_product(5,8,10))
