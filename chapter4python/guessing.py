import random

def guess_right_number_lovelies(number):

    random_number = random.randint(1,1000)
    print(random_number)
    users_guess = int(input("Guess the number loveies  and press 0 to stop = "))

    while users_guess != 0:
        if users_guess == random_number:
            return"Congratulation 🥰️🤩️ !!!! "
        elif users_guess > random_number:
            print("Too high 🥰️ keep trying!! ")
            users_guess = int(input("Guess the number loveies  and press 0 to stop = "))
        elif users_guess < random_number:
            print("Too low  🥰️ keep going !!")
            users_guess = int(input("Guess the number loveies  and press 0 to stop = "))

print(guess_right_number_lovelies(9))
