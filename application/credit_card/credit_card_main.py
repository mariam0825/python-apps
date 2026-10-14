from credit_card import validate_credit_card


print("+++++++++++++++++++++++++++++++++++++")
print("       CREDIT CARD VALIDATOR")
print("======================================")

card_number = input("Enter your credit card number: ")

card_type, valid = validate_credit_card(card_number)

print("\nCard Type:", card_type)

if valid:
    print("Status: Valid")
else:
    print("Status: Invalid")



