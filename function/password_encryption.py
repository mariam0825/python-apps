class password_encryption:
    def __init__(self, password):
        self.password = password

    def encryption(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        password_code = ""

        for letter in self.password.casefold():
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = ((position + 13) % 26)
                password_code += alphabet[new_position]
            else:
                 password_code += letter

        return  password_code


password = password_encryption("hello world!")
print(password.encryption())

