from datetime import datetime
from check_out_function import check_out_function


def main():

    checkout = check_out_function()

    print("======================================")
    print("            SEMICOLON STORE")
    print("======================================")

    customer_name = input("What is Customer's name: ")

    while True:
        print("\n1. Add Item")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

       
        if choice == 1:

            item_name = input("What did the user buy? ")

            quantity = int(input("How many pieces? "))

            price = float(input("How much per unit? "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                continue

            if price < 0:
                print("Price cannot be negative.")
                continue

            checkout.products.append(item_name)
            checkout.quantity.append(quantity)
            checkout.price.append(price)

            print("\nItem added successfully!")

       
        elif choice == 2:

            if len(checkout.products) == 0:
                print("\nYour cart is empty.")
                continue

            print("\n======================================")
            print("                CART")
            print("======================================")

            for count in range(len(checkout.products)):

                item = checkout.products[count]
                quantity = checkout.quantity[count]
                price = checkout.price[count]

                total = price * quantity

                print(f"{count + 1}. "
                    f"{item} | "
                    f"Qty: {quantity} | "
                    f"Price: ₦{price:.2f} | "
                    f"Total: ₦{total:.2f}")

            print("======================================")

       
        elif choice == 3:

            if len(checkout.products) == 0:
                print("\nYour cart is empty.")
                continue

            print("\n======================================")
            print("              CHECKOUT")
            print("======================================")

            cashier_name = input("What is Cashier's  name? ")

            discount = float(input("How much discount will he get? "))

            subtotal = 0

            for count in range(len(checkout.products)):

                subtotal += checkout.check_for_total_price_of_product(
                    checkout.products[count],
                    checkout.price[count],
                    checkout.quantity[count])

            discount_amount = subtotal * discount / 100
           
            price_after_discount = subtotal - discount_amount

            vat_amount = price_after_discount * 7.5 / 100

            bill_total = price_after_discount + vat_amount

        

            print("\n")
            print("=" * 70)
            print("                 SEMICOLON STORE")
            print("                 MAIN BRANCH")
            print("=" * 70)

            print(
                "LOCATION: 312, HERBERT MARCAULAY WAY, "
                "SABO YABA, LAGOS."
            )

            print("TEL: 03293828343")
            print("Date:", datetime.now())
            print("Cashier:", cashier_name)
            print("Customer:", customer_name)

            print("-" * 70)

            print(
                f"{'ITEM':<20}"
                f"{'QTY':<10}"
                f"{'PRICE':<15}"
                f"{'TOTAL':<15}"
            )

            print("-" * 70)

            for count in range(len(checkout.products)):

                item = checkout.products[count]
                quantity = checkout.quantity[count]
                price = checkout.price[count]

                total = price * quantity

                print(
                    f"{item:<20}"
                    f"{quantity:<10}"
                    f"₦{price:<14.2f}"
                    f"₦{total:<14.2f}"
                )

            print("-" * 70)

            print(f"{'Sub Total:':<40} ₦{subtotal:.2f}")
            print(f"{'Discount:':<40} ₦{discount_amount:.2f}")
            print(f"{'VAT @ 7.5%:':<40} ₦{vat_amount:.2f}")

            print("=" * 70)

            print(f"{'Bill Total:':<40} ₦{bill_total:.2f}")

            print("=" * 70)

            print(
                f"THIS IS NOT A RECEIPT "
                f"KINDLY PAY ₦{bill_total:.2f}"
            )

            print("=" * 70)

            amount_paid = float(
                input("How much did the customer give to you? ")
            )

            balance = amount_paid - bill_total

            print(f"{'Amount Paid:':<40} ₦{amount_paid:.2f}")
            print(f"{'Balance:':<40} ₦{balance:.2f}")

            print("=" * 70)
            print("        THANK YOU FOR YOUR PATRONAGE")
            print("=" * 70)

            break

    
        elif choice == 4:

            print("Thank you for using Semicolon Store.")
            break

        else:
            print("Invalid choice. Please try again.")



