
from arithmetic_function import calculate_question, get_questions, calculate_time_taken
exit = 1

menu = """
	Welcome To Simple Arithmetic Application
	
	1. Take Questions
	
	0. Exit
    
"""
print(menu)
user_choice = input("Enter option: ")
from datetime import
while(exit !=0):

    if user_choice == "1":
        start_time = datetime.now().second
        score = 0

        for _ in range(10):
            first_number, second_number = get_question()

            user_answer = int(input (f"Solve : \n\t {first_number} - {second_number}\t Answer: "))

            result = calculate_question(first_number, second_number)

        if  user_answer == result:

            score += 1
            end_time = datetime.now().second
            time_taken = calculate_time_taken(start_time, end_time
            
            time_taken
            print(f"Your score is {score}")

            to_continue = input ("Do you wish to continue:  Yes?No")

        if to_continue.lower() == "yes":
            continue
        else:
            print("You don try!!! \n Oya go rest")
            exit = 0
    else:
    
        exit = 0
