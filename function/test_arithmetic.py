
import unittest

from arithmetic_function import *
class SimpleArithemeticTest(unittest.TestCase):

    def test_that_a_number_is_generated_randomly(self):

        lower_range = 50
        higher_range = 100
        random_number = generate_random_number(lower_range, higher_range)

        self.assertTrue(random_number< higher_range)
        self.assertTrue(random_number >= lower_range)

    def test_that_get_question_function_returns_two_random_numbers_for_the_question(self):

        number_one , number_two = get_question()
    
        self.assertIsNotEqual(number_one, number_two)
        self.assertTrue(number-one > number_two)

    def test_question_is_calculated_and_answer_is_given_accurately(self):
    
        number_one = 50
        number_two = 20
    
        result = calcualte_question(number_one , number_two)
    
        self.assertEqual(result,number_one - number_two)
        self.assertIsNotNone(result)
        
    def test_that_improper_question_is_not_calculated_NoneIsReturned(self):
    
        print("This is G test")
        number_one = 50
        number_tw0 = 200
        
        result = calculate_question(number_one , number_two)
        self.assertEqual(result, None)
        self.assertIsNone(result)
        
    def test_that_time_taken_for_answering_questions_is_calculated(self):
        
      
       import time
       import math
        
        start_time = time.perf_counter()
        
        time.sleep(10)
        
        end_time = time.perf_counter()
        time_taken = calculate_time_taken(start_time, end_time)
        time_in_sec = math.floor(time_taken)
        self.assertEqual(time_taken, 10)
        

        
