odd_number= 0
even_number = 0
#numbers = int(input("Enter numbers seperated by commas: ")
numbers = [2, 3, 5, 8, 9]
for number in numbers:
	if number % 2 ==0:
		even_number+=1
	else:
		odd_number+=1
print(f'The number of even numbers is {even_number}')
print(f'The number of odd number is {odd_number}')

