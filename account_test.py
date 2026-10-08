import unittest
from account import *

class accountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account = Account("Winifred")
        self.assertEqual(account.balance,0)
        self.assertEqual(account.name,"winifred")

    def test_that_account_can_recieve_deposit(self):
        account = Account("Winifred")
        account.deposit(2500)
        self.assertEqual(account.balance,2500)

    def test_that_account_cannot_recieve_a_negative_amount(self):
        account = Account("Winifred")
        self.assertRaises(ValueError, account.deposit,-2500)

    def test_that_account_can_withdraw_from_amount(self):
        account = Account("Winifred")
        account.deposit(2500)
        account.withdraw(1500)
        self.assertEqual(account.balance,1000)

    def test_that_account_cannot_recieve_more_Than_balance(self):
        account = Account("Winifred")
        self.assertRaises(ValueError, account.withdraw, 4000)





if __name__=='__main__':
    unittest.main()
