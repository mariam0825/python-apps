import unittest

from check_out_function import *
class checkOutSystemTest(unittest.TestCase):
    
    def test_that_product_can_be_added(self):
        item_name = "soap"
        price = 5000.00
        quantity = 1
        
        self.assertEqual(1 ,check_product_quantity("item_name" , 200 , 2))

    def test_that_product_Price_can_be_added(self):
        item_name = "biscuit"
        price = 2000.00
        quantity = 1
        
        self.assertEqual(1 ,check_product_price("item_name" , 2000 , 1))

    def test_that_negative_Price_cannot_be_added(self):
        item_name = "biscuit"
        price = -2000.00
        quantity = 1
        
        self.assertFalse(False ,check_negative_price("item_name" , 2000 , 1))

        
    def test_that_product_more_one_product_can_be_added(self):
        item_name = "soap"
        price = 5000.00
        quantity = 2
        item_name_one = "biscuit"
        price_one = 2000.00
        quantity_one = 4
        
        self.assertEqual(2 ,check_for_more_products("item_name", 2000, 2))
    
    def test_that_product_quantity_can_be__more_one_product(self):
        item_name = "soap"
        price = 5000.00
        quantity = 2
        item_name_one = "biscuit"
        price_one = 2000.00
        quantity_one = 4
        
        self.assertEqual(2 ,check_for_more_products_quantity("item_name", 2000, 6))

    def test_that_total_price_of_product_can_be_added(self):
        item_name = "soap"
        price = 5000.00
        quantity = 2
        
        self.assertEqual(10000.00 ,check_for_total_price_of_product("item_name", 2000, 2))

    def test_that_total_price_of_product_of_quantity_can_be_added(self):
        item_name = "soap"
        price = 5000.00
        quantity = 2
        item_name_one = "biscuit"
        price_one = 2000.00
        quantity_one = 2

        self.assertEqual(14000.00 ,check_for_total_price_of_product_quantity("item_name", 2000, 6))

    
    def test_that_you_delete_product(self):

        item_name = "soap"
        price = 5000.00
        quantity = 2
        item_name_one = "biscuit"
        price_one = 2000.00
        quantity_one = 2
        
        self.assertEqual(1 ,check_for_deleting_of_product("item_name", 2000, 2))

    def test_that_price_that_can_be_gotten_after_discount(self):
        item_name = "soap"
        price = 9000.00
        quantity = 5
        item_name_one = "biscuit"
        price_one = 5000.00
        quantity_one = 10
        
        discount = 10
        expected_price = 85000.00
        actual_price = 95000.00
        self.assertEqual(expected_price , actual_price-                                     check_for_discounted_price(item_name, 2000, 2)
)

    def test_that_price_can_be_gotten_after_Vat(self):

        item_name = "soap"
        price = 9000.00
        quantity = 5
        item_name_one = "biscuit"
        price_one = 5000.00
        quantity_one = 10
        
        discount = 10
        discount_amount = 8500.00
        expected_vat = discount_amount * 7.5 / 100 + discount_amount
        actual_price = 91375
        self.assertEqual(expected_vat , actual_price-actual_price - check_for_price_after_vat(...) == 9137.5








    


    








