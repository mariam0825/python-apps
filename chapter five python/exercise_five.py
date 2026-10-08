def eliminate_duplicate(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers

numbers = [5, 2, 3, 5, 3, 4, 3, 2, 7, 1, 8, 6, 6]

print(eliminate_duplicate(numbers))

