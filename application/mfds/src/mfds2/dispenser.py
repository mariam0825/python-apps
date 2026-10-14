
from src.mfds2.fuel import Fuel
class Dispenser:
    def __init__(self):
        self.fuel = {}
        self.transactions = []

    def add_fuel(self, fuel_name, price, quantity):
        if fuel_name in self.fuel:
            return False
        fuel = Fuel(fuel_name, price, quantity)
        self.fuel[fuel_name] = fuel
        return True

    def get_price_per_litre(self, fuel_name):
        if fuel_name in self.fuel:
            return self.fuel[fuel_name].get_amount_per_litre()
        return None

    def get_number_fuel_type_available(self):
        return len(self.fuel)

    def get_available_fuel(self):
        return self.fuel

    def clear(self):
        self.fuel.clear()
        self.transactions.clear()

    def update_price(self, fuel_name, new_price):
        if fuel_name not in self.fuel or new_price <= 0:
            return False
        self.fuel[fuel_name].set_amount_per_litre(new_price)
        return True

    def restock(self, fuel_name, quantity):
        if fuel_name not in self.fuel or quantity <= 0:
            return False
        self.fuel[fuel_name].update_quantity(quantity)
        return True

    def get_available_fuel_quantity(self, fuel_name):
        if fuel_name in self.fuel:
            return self.fuel[fuel_name].quantity
        return None

    def dispense_with_amount(self, fuel_name, amount):
        if fuel_name not in self.fuel or amount <= 0:
            return False
        fuel = self.fuel[fuel_name]
        litres = amount / fuel.get_amount_per_litre()
        if litres > fuel.get_quantity():
            return False
        fuel.sell(litres)
        self.transactions.append({'fuel_name': fuel_name,'litres': litres, 'total_amount': amount})
        return litres

    def dispense_with_quantity(self, fuel_name, litres):
        if fuel_name not in self.fuel or litres <= 0:
            return False
        fuel = self.fuel[fuel_name]
        if litres > fuel.get_quantity():
            return False
        total_amount = litres * fuel.get_amount_per_litre()
        fuel.sell(litres)
        self.transactions.append({'fuel_name': fuel_name,'litres': litres,'total_amount': amount})
        return total_amount

    def dispense_fuel(self, fuel_name, amount, buy_with):
        if buy_with == "amount":
            return self.dispense_with_amount(fuel_name, amount)
        elif buy_with == "quantity":
            return self.dispense_with_quantity(fuel_name, amount)
        return False

    def show_all_transactions(self):
        return self.transactions


