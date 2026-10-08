def nested_loop (numbers):
    count = 1
    for row in range(2):
        for column in range(3):
            numbers[row][column] = count
            count += 1

    return numbers


numbers = [ [0,0,0],
            [0,0,0] ]

print(nested_loop(numbers))

