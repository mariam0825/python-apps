class fuel_products(object):
    def __init__(self ,product_name: str,amount_per_litre: float,litres: int,total_amount: int):
        self.product_name = product_name
        self.amount_per_litre = amount_per_litre
        self.litres = litres
        self. total_amount = total_amount

    def product_name(self, product_name: str):
        self. product_name = product_name


    def litres_increase(self, litres: int):
        self.litres = litres
        count = 0
        for fuel in range(litres):
            count += 1
        self.litres = count
        self.total_amount = self.amount_per_litre * self.litres

    def negative_litres(self, litres: int):
        self. litres  = litres
        if self.litres >= 0:
            raise ValueError("Cannot enter nagetive litres")
        self. litres = litres
    def non_Product(self,product_name: str):
        self.product_name = product_name
        if self.product_name != "Water":
            raise ValueError("Oga na fuel we dey sell !!!")
        self.product_name = product_name