sum = 0
counter = 0
#number = int(input("Enter positive numbers: "))
for number in range(10):
	number = int(input("Enter positive numbers: "))

	sum += number
	counter+=1
	
	average = sum/counter
	
print(f'The average of the numbers is {average}')
