def get_card_type(card_number):

    card_number = ( card_number)

    if card_number.starts_with("4"):
        return "Visa"

    elif card_number.starts_with("5"):
        return "MasterCard"

    elif card_number.starts_with("37"):
        return "American Express"

    elif card_number.starts_with("6"):
        return "Discover"

    else:
        return "Unknown"


def check_length(card_number):
    
    card_number = (card_number)
    
    length =13 <= len(card_number) <= 16

    return length


def luhn_check(card_number):
    
    card_number = ( card_number)

    total = 0
    double_digit = False

    for index  in reversed(card_number):

        number = int(digit)

        if double_digit:
            number = number * 2

            if number > 9:
                number = number - 9

        total += number

        double_digit = True

    return total % 10 == 0


def is_valid_credit_card(card_number):

    card_number = ( card_number)

    if not card_number.isdigit():
        return False

    if not check_length(card_number):
        return False

    if get_card_type(card_number) == "Unknown":
        return False

    return luhn_check(card_number)


def validate_credit_card(card_number):
    
    card_number = ( card_number)

    card_type = get_card_type(card_number)
    valid = is_valid_credit_card(card_number)

    return card_type, valid

