number = int(input("Enter a number to find its exponentiation: "))

power = 2
result = 1

for _ in range(power):
	
	result *= number

print(result)
