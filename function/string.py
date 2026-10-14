def count_letter(word,letter):

    count = 0
    for char in word :
        if char == letter:
            count+=1

    return count



def is_palindrome(word):
    reversed_word = ""

    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]

    return word == reversed_word


def longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print (count_letter("My madam", "m"))
