def positive_number(number):
    
    positives = []
    for value in number:
        if value > 0:
            positives.append(value)
            
    
    if len(positives) == 0:
        return 0

    smallest = positives[0]
    
    largest = positives[0]  
   
    for value  in  positives:
   
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

        else:
        
            result = largest - smallest

    return result


number = {2,5,1,9,7}
print(positive_number(number))
    

        
        
