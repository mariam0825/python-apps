#import unittest

from unittest import TestCase

from account_function import *
#class AccountTest(TestCase):

   # def test_sample(self):
      #  result = 15

        #first_number = 10

        #second_number = 5

       # summation = first_number + second_number
        

        #self.assertTrue(summation == result)

        #self.assertEqual(summation , result)

class AccountTest(TestCase):
    
    def test_accountBalance_isZero_duringCreation(self):
        expected_balance = 0

        actual_balance = check_balance(0.0)
       
        self.assertEqual(actual_balance , expected_balance)


    def test_thatAccount_canBeDepositedInto_afterCreation(self):
        amount = 500.0

        self.assertEqual(0.0, check_balance(0.0))

        balance = deposit(amount)

        self.assertEqual(500.0, check_balance(balance))

    def test_thatAccountCanBeDespositedInto_twice(self):
        first_amount = 3000.0

        second_amount = 2500.0

        initial_bal = 0.0

        self.assertEqual(0.0, check_balance(0.0))

        balance = deposit(first_amount, balance)

        self.assertEqual(3000.0, check_balance(balance))


        second_balance = deposit(second_amount, balance)

        self. assertEqual(5500.0, check_balance(second_balance))


    def test_DepositNeagtiveAmount_balanceRemains_unchanged(self) :

        initial_bal = 0.0
        self.assertEqual(0.0, check_balance(initial_bal))

        new_balance = deposit(3500,initial_bal)

        self.assertEqual(3500, check_balance(new_balance))

        unchanged_balance = deposit(-200 , new_balance)
        
        self.assertEqual(3500, check_balance(unchanged_balance))

    def test_thatAccountWithdrawal_withdrawsAccurate_Amount(self):

        initial_bal =0.0

        balance = deposit(5000, initial_bal) 

        self. assertEqual(balance, 5000.0)

        new_balance = withdraw(3000.0, balance)

        self.assertEqual(new_balance, 2000.0)  


    def test_that_AccountWithdrawal_is_not_above_above(self)

        initial_bal = 0.0

        balance =deposit(3000, initial_balance)

        self.assertEqual(balance, 3000.0)

        new_balance = withdraw(5000 , balance)

        self.assertEqual(new_balance, 3000.0)
        
        self.assertTrue(new_balance == 3000.0)

    def test_that_AccountWithdrawal_is_not_Valid(self)

        initial_bal = 0.0

        


    












        










