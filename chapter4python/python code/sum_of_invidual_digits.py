sum = 0
number = int(input("Enter a positive number: "))

while number > 0:
	digit = number % 10
	sum+=digit
	number//=10
print(f'The sum of digits in number is {sum}')
