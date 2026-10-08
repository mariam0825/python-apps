
counter = 1

number = int(input("Enter positive numbers: "))
while number > 1:
	if number % 2 ==0:
		number = number/2
		counter+=1
	else:
		number = number * 3 + 1
		counter+=1
	
print(counter)