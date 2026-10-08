def check_perfect_square(numbers):
    digit = []
    for number in numbers:
        for index in range(number + 1):
            if index * index == number:
                digit.append(True)
                break 
        else:
            digit.append(False)

    return digit


numbers = [0,1,2,3,4,9,10,16,25,26]

print(check_perfect_square(numbers))
