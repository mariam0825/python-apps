def prime_number (number):
    for values in range(2,1000):
     
        if is_prime(number):
            print(number)
    
        if number < 2:
            return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

number = 1000
print prime_number(number)
