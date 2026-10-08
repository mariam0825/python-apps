
balance = 1000

option = 8
while (option !=0):

    print("""Welcome to Orion Banks
 1. Deposit
 2. Withdraw
 3. Check Balance
 0. Exit
 """)

    option  = input("Choose an option")
    match(option):

        case "1":
            amount = int(input("Enter amount to deposit: "))
            balance+=amount

        case "2":
            amount = int(input("Enter amount to withdraw: "))
            if balance < amount:
                print("Insufficient fund")
                break
            balance-=amount
    
        case "3":
            print(balance)

        case "0":
            option = 0
