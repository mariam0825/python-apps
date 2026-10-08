
sum = 0

number = int(input("Enter a number: "))

for number in range(number+1):

	sum = sum + number
	
	number+=1

print(f'The sum of the numbers in number is {sum}')
