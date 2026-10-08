
print(">>>>>>>> WELCOME TO ORION GAMING HUB<<<<<<<<<<<<<<<")

number = int(input("Guess a number within 1 to 100 to reveal the secret number: ")) 
	
secret_number = 49
if (number == secret_number):
		
	print("Congratulations, you guessed right!!!")

if (number<=30 and number !=49):
	print("number too low to secret number, try again!!!")

if (number>30 and number <49):
	print("Getting closer, try one more time!!!")

if (number>=70 and number != 49):
	print("number too high to secret number, try again!!!")
if (number >49 and number <70):
	print("Getting closer, try one more time!!!")
	
if (number > 100 or number < 0):
	print("Invalid Entry")

	
