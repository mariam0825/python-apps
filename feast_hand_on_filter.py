list_in_list = [1, None, 3, None, 5, None, 7]

def list_none_in_list(value):
    return value is not None

remove = list(filter(list_none_in_list, list_in_list))
print(remove)


# number divislbe three ---------------
number = [1, 3, 4, 6, 9, 10]

def number_divisible_three(value):
    return value % 3 == 0

result = list(filter(number_divisible_three, number))
print(result)

# positive number ----------------
number = [-2,-1,0,1,2]

def positive_number(digit):
    return digit > 0
result = list(filter(positive_number, number)) 
print(result)

# age that is greater than 25----------------

people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]

def age_greater_than_25(person):
    return person['age'] > 25

result = list(filter(age_greater_than_25, people))
print(result)

