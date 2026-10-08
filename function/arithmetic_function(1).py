
#My Arithmetic Application 

"""Generate the first random Number

Generate the second random Number that cannot be higher than the first random number

#check that the second random is not higher than the first random number
#switch the number if the second random is higher than the first random number

display the subtraction of the second from the first number as a question
create a time reference to keep track of the amount of time spent on the whole questions 
allow the user to enter and  answer for the question
Take the answer and assign it to a reference or a container
calculate and get the result of the subtraction of the second number from the first number
Assign the result of the above calculation to a reference or container called correct-answer
compare the user's inputted answer to correct container
create a reference that keeps track of the number of accurately answered questions
increase the value of the reference by one for every correct answer question by the user
Give the user two attempts when they answer wrongly before moving to the next question
Repeat the entire process ten times and for each time you track the value of score
Display score

Display the total amount of the time spent on the whole question

"""


import random

def generate_random_number(lower_band , higher_band):

    generated_number = random.randrange(lower_band, higher_band)
    return generated_number
    
def get_questions():
    
    first_number = generate_random_number(100, 500)
    second_number = generate_random_number(100, first_number)
   
    question = [first_number, second_number]
    return question
    
def calculate_question(first_number, second_number):
    if first_number > second-number:
        return first_number - second_number
    
def calculate_time_taken(start_time, end_time):

    return end_time - start_time
    






