import unittest

from credit_card import *
class CreditCardTest(unittest.TestCase):

    def test_that_card_length_is_valid(self):
        self.assertTrue(check_length("4388576018410707"))

    def test_that_card_length_less_than_13_is_invalid(self):
        self.assertFalse(check_length("43885760184"))

    def test_that_card_length_more_than_16_is_invalid(self):
        self.assertFalse(check_length("438857601841070712"))

    def test_that_visa_card_is_recognized(self):
        self.assertEqual("Visa", get_card_type("4388576018410707"))

    def test_that_mastercard_is_recognized(self):
        self.assertEqual("MasterCard", get_card_type("5123456789012345"))

    def test_that_american_express_is_recognized(self):
        self.assertEqual("American Express", get_card_type("371234567890123"))

    def test_that_discover_card_is_recognized(self):
        self.assertEqual("Discover", get_card_type("6123456789012345"))

    def test_that_unknown_card_is_rejected(self):
        self.assertEqual("Unknown", get_card_type("7123456789012345"))

    def test_that_valid_card_passes_luhn_check(self):
        self.assertTrue(luhn_check("4388576018410707"))

    def test_that_invalid_card_fails_luhn_check(self):
        self.assertFalse(luhn_check("4388576018402626"))

    def test_that_valid_credit_card_is_valid(self):
        self.assertTrue( is_valid_credit_card("4388576018410707"))

    def test_that_invalid_credit_card_is_invalid(self):
        self.assertFalse(is_valid_credit_card("4388576018402626") )

    def test_that_invalid_card_type_is_invalid(self):
        self.assertFalse(is_valid_credit_card("7123456789012345"))

    def test_that_validate_credit_card_returns_type_and_status(self):
        result = validate_credit_card("4388576018410707")

        self.assertEqual(("Visa", True), result)




