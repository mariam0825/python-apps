from account_function import *



balance = 0
 
print("Welcome to Orion Account...........")

menu = """

    1. Check Balance

    2. Deposit

    3. Withdrawal

    0. Exit

        """

tracker = 1

while(tracker !=0):
    choice = float(input(f"{meun}\nEnter Your Choice : " ))

    match Choice:

        case "1":
                courrent_balance = Check_balance(balance)

                print(f"Your Account Balance: {current_balance}")

        case "2":
                amount = input("Enter your Amount to deposit :")

                for digit in amount;
                   if  not digit.isdigit():
                        print("invalid")
                        break
                else:
                    amount= float(amount)

                new_balance = deposit(balance, amount)

                if new_balance == balance:
                    print("Invalid Amount Inputted")

                else:
                    balance = new_balance
                    print("Deposit was successful")

        case "3":
                amount = float(input("Enter your Amount to deposit :"))

                new_balance = withdraw(balance, amount)

                if new_balance == balance:
                    print("Invalid Amount Inputted")

                else:
                    balance = new_balance
                    print("Deposit was successful")

        case "0":
                print("Oya oga go Rest !!!!")
                tracker = 0

        case _:
               print("Get sense na !!!!")
               break
