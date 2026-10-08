import unittest
from fuel_function import *

class FuelTest(unittest.TestCase):
    def test_For_types_for_different_type_of_fuel_product(self):
        fuel_product = fuel_products("Petrol", 750 , 1, 750)
        self.assertEqual(fuel_product.product_name,"Petrol")
        self.assertEqual(fuel_product.amount_per_litre, 750)
    def test_for_kerosene_and_it_own_price(self):
        fuel_product = fuel_products("kerosene", 650, 1, 650)
        self.assertEqual(fuel_product.product_name,"kerosene")
        self.assertEqual(fuel_product.amount_per_litre, 650)

    def test_for_Diesel_and_it_own_price(self):
        fuel_product = fuel_products("Diesel", 1100, 1,1100)
        self.assertEqual(fuel_product.product_name, "Diesel")
        self.assertEqual(fuel_product.amount_per_litre, 1100)

    def test_for_Gas_and_it_own_price(self):
        fuel_product = fuel_products("Gas", 1300,1, 1300)
        self.assertEqual(fuel_product.product_name,"Gas")
        self.assertEqual(fuel_product.amount_per_litre, 1300)

    def test_for_increase_in_litre(self):
        fuel_product = fuel_products("petrol" , 750, 8, 6000)
        self.assertEqual(fuel_product.product_name, "petrol")
        self.assertEqual(fuel_product.litres , 8)

    def test_for_calculating_the_amount_of_products_according_to_litre(self):
        fuel_product = fuel_products("petrol" , 750, 8,6000)
        self.assertEqual(fuel_product.product_name, "petrol")
        self.assertEqual(fuel_product.amount_per_litre, 750)
        self.assertEqual(fuel_product.litres, 8)
        self.assertEqual(fuel_product.total_amount, 6000)
    def test_For_nagative_litres(self):
        fuel_product = fuel_products("petrol" , 750, -1, 6000)
        self.assertEqual(fuel_product.product_name, "petrol")
        self.assertTrue(fuel_product.litres, -1)
    def test_for_non_product(self):
        fuel_product = fuel_products("Water", 1100, 1, 1100)
        self.assertTrue(fuel_product.product_name, "Water")

    def test_for_zero_litres(self):
        fuel_product = fuel_products("petrol" , 750, 0, 6000)
        self.assertEqual(fuel_product.product_name, "petrol")
        self.assertFalse(fuel_product.litres, 0)