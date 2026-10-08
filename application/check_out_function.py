class check_out_function:

    def __init__(self):
        self.products = []
        self.quantity = []
        self.price =[]
        

    def check_product_quantity(self, item_name, price, quantity):
        if quantity < 0:
            return False

        self.products.append(item_name)
        self.quantity.append(quantity)
        return quantity

    def check_product_price(self, item_name, price, quantity):
            if price < 0:
                return False

            self.price.append(price)
            return quantity

    def check_negative_price(self, item_name, price, quantity):
            return price >= 0

    def check_for_more_products(self, item_name, price, quantity):
            self.products.append(item_name)
            self.price.append(price)
            self.quantity.append(quantity)

            return len(self.products)

    def check_for_more_products_quantity(self, item_name, price, quantity):
             return quantity

    def check_for_total_price_of_product(self, item_name, price, quantity):
         return price * quantity

    def check_for_total_price_of_product_quantity(self, item_name, price, quantity ):
            return price * quantity

    def check_for_deleting_of_product(self, item_name, price, quantity):
            if item_name in self.products:
                index = self.products.index(item_name)

                self.products.pop(index)
                self.price.pop(index)
                self.quantity.pop(index)

            return len(self.products)

    def check_for_discounted_price(self, item_name, price, quantity):
            """
            Calculates the price after a 10% discount.
            """
            total = price * quantity
            discount = total * 10 / 100
            return total - discount

    def check_for_price_after_vat(self, item_name, price, quantity):
            """
            Calculates the price after a 7.5% VAT.
            """
            total = price * quantity
            vat = total * 7.5 / 100
            return total + vat
