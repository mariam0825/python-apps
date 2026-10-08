

from unittest import TestCase
from range_positive_number import postive_number



class range_postive_number(TestCase):

    def test_range_positive_number(self):

       number = {1,2,3,5,7,9}
       result = 8
       actual_result = positive_number(number)
        

       self.assertEqual(actual_result , result)


    def test_number_WithNegative_numberRemain_unchange(self):

        number = {-1, -2, 5,10, 7}

        result = 5

    
        calculation = smallest - largest
       
        actual_result = positive_number(number)
    
        

        self.assertEqual(actual_result, result)

























    
















