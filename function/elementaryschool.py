import random



def generate_number():
    return (random.randint(1,9),random.randint(1,9))

def Multiplcation():
    passed = 0;
    failed = 0
    
    number1, number2 = generate_number()
    answer = number1 * number2
    user_input = input(f"How much is {number1} times {number2} enter 0 to end:")
    while True:

        if int (user_input) == answer:   
            passed += 1
            counter_for_pass(passed)
           
        else:
            failed += 1
            counter_for_fail(failed)

        user_input = input(f"do you want to continue?how much is {number1} times {number2} enter 0 to end:")
        if(user_input == 0): break;


def counter_for_pass(number):
    
    match(number):
        case 1: print("wow, nice first attempt")
        case 2: print("very good")
        case 3: print("keep up the good work")
        case _: print("Nice work")

def counter_for_fail(number):
    match(number):
        case 1: print("nice try for first attempt but try again")
        case 2: print("keep going youre there")
        case 3: print("No, keep tring")
        case _: print("proud of you but go again")

print(Multiplcation())
    
