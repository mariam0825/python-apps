new_number = 0

number = int(input("Enter string of numbers: "))

while number > 0:

	remainder = number % 10
	new_number = new_number * 10 + remainder
	number = number//10

print(new_number)

	