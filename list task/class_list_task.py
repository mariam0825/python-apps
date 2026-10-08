import math

def perfect_square(numbers):
    digit = []
    for index in numbers:

        number_sqrt = int(math.sqrt(index))

        if (index == number_sqrt **2):

            digit.append(True)
           
        else:

            digit.append(False)

    return digit

numbers = [4,9,25,49,8,5,36,7]

print(perfect_square(numbers))
