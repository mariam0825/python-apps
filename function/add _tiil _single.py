def digit_sum_all_single(number):
    while number >= 10:
        result = 0;
        while number > 0:
            digit = number % 10
            result += digit
            number = number //10
            number = result
        return number
print(digit_sum_all_single(9875))
