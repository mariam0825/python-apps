number = int(input("Enter a number to check if it is a prime number: "))

def is_prime(number):
	for count in range(2,number//2 + 1):
		if number%count == 0:
			return False

	return True

def all_prime(number):
	prime_numbers= []
	for counter in range(2, number +1):
		if is_prime(counter) == True:
			prime_numbers.append(counter)
	return prime_numbers
print(all_prime(number))

