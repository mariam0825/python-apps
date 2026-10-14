from fuel_function import fuel_products
exit = 1
menu = """
    Welcome To Mariam's fuel Dispenser Application

    1. Buy Petroleum
    2. Show Transaction history
    0. Exit
    
"""
fuel_product = fuel_products()
print(menu)
user_choice = input("Which product would you like to buy? : ")
while exit != 0:
    print(menu)
    user_choice = input("Which product would you like to buy? : ")
    if user_choice == "1":
        fuel_product = fuel_products(user_choice)
        product_name( product_name)
        fuel_menu = """
            
            1. Petrol  =>  750 / liter
            2. Diesel   => 1100/ liter
            3. Kerosene => 650/liter
            4. Gasoline  => 1300/liter

        """
    fuel_product = fuel_products(product_name , litres)
    print(fuel_menu)
    user_choice = input("Which product would you like to buy? : ")
    if user_choice == "1":
        fuel_product = fuel_products(user_choice)
        print("How many liters would you like? ")
        litres = int(input())







