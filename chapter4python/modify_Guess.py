import random

def guess_right_number_lovelies(number):

    random_number = random.randint(1,1000)
    print(random_number)
    guess_count = 0
    users_guess = int(input("Guess the number 🤩️  or press 0 to stop = "))
    guess_count +=1

    while users_guess != 0:
        
        users_guess = int(input("Guess the number 🤩️  or press 0 to stop = "))
        guess_count +=1

        if users_guess == random_number:
            return"Congratulation 🥰️🤩️ !!!! "
        elif users_guess > random_number:
            print("Too high 🥰️ keep trying!! ")
            
        elif users_guess < random_number:
            print("Too low  🥰️ keep going !!")
            
            

        if guess_count <= 10:
            print("Either you knew the secrect or you got lucky 😁️!!")
        else:
            print("You should be able to do better💪️!! ")

print(guess_right_number_lovelies(10))
