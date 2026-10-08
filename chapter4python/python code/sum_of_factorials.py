sum = 1
number =1
number = int(input("Enter a number: "))

for number in range(number+1):
	if number>=1:
		sum*= number
	
		number-=1

print(f'The sum of number! is {sum}')
