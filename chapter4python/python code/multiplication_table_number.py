
number = int(input("Enter a number: "))

for number in range(number , 11):
	
	for counter in range(number , 11):
		if counter==number:
			result = counter * number
			print(f'{number} X {counter} = {result}', end="\t")
		break

	print(" ")
	
