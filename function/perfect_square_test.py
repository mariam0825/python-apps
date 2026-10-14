import unittest

from perfect_square import *
class perfectSquareTest(unittest.TestCase):

    def test_that_perfect_number_should_return_True(self):
        numbers = [0,1,2,3,4,6,9,10,16,25,26]
        
        actual_result= [True,True,0,0,True,True,0,True,True]
        self.assertTrue(actual_result,check_perfect_square(numbers)) 

    def test_that_number_that_not_perfect_number_should_be_false(self):
        numbers = [0,1,2,3,4,6,9,10,16,25,26]
        
        actual_result = [0,0,False,False,0,0,False,0,0]
        self.assertTrue(actual_result,check_perfect_square(numbers)) 


    
