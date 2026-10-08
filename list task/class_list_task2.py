def palindrome_list (texts):
    result = []
    for index in texts:
        if(index == index [ ::-1]):
            result.append(True)
        else:
            result.append(False)
    return result


texts = ["Madam", "hello", "noon","racecar"]

print(palindrome_list(texts))
