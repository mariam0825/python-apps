from functools import reduce

def sum_up(accumulator, number):

    return accumulator + number
    
    
numbers = [1,2,3,4,5]

result = reduce(sum_up, numbers)

print(result)


# product -------------

def product(accumulator, number):

    return accumulator * number
    
    
numbers = [2,3,4,]

result = reduce(product, numbers)

print(result)

# concatenate --------------

def concatenate(accumulator, string):

    return accumulator + string
    
    
word = ["\"Hello", "World\""]

result = reduce(sum_up, word)

print(result)

# dictionary ----------------
def merge_dicts(accumulator, dictionary):
    accumulator.update (dictionary)
    return accumulator

diction = [{'a': 1}, {'b': 2}, {'c': 3}]

result = reduce(merge_dicts, diction, {})
print(result)


# summ of square ----------------

def sum_of_square(accumulator, number):

    return accumulator + number **2
    
    
numbers = [2,3,4,]

result = reduce(sum_of_square, numbers)

print(result)




