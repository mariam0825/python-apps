def convert_to_integer(digit):
    return int(digit)

values = ["1","2","3"]
print(list(map(convert_to_integer, values)))

def adding_10_To_each_element(values):
    return int(values) +10

numbers = [0,5,10,15]
print(list(map(adding_10_To_each_element,numbers)))

def convert_temperatureCelsius_to_fahrenheit(celsius):

    return int(celsius) *1.8 +32

temperature = [0,20,37,100]
print(list(map(convert_temperatureCelsius_to_fahrenheit, temperature)))
