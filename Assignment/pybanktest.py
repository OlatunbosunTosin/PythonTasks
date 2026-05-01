import unittest
import pybank

class TestEmailValidationFunction(unittest.TestCase):

    def test_that_validate_email_exists(self):
        pybank.validate_email("Tosin@1234")

    def test_that_email_is_at_least_eight_characters(self):
        expected = pybank.validate_email("Tosin@1234")
        self.assertTrue(expected)

    def test_that_email_is_less_than_eight_characters(self):
        expected = pybank.validate_email("To@1234")
        self.assertFalse(expected)

    def test_that_email_contains_at_symbol(self):
        expected = pybank.validate_email("To@sin")
        self.assertFalse(expected)        
       
    def test_that_invalid_email_raise_value_error(self):
        self.assertRaises(ValueError,pybank.validate_email, "Tosin")        
       
    def test_that_valid_email_doesnot_start_with_at(self):
        expected = pybank.validate_email("@Tosin")
        self.assertEqual(expected, "Invalid email")

    def test_that_valid_email_does_not_end_with_at(self):
        expected = pybank.validate_email("Tosin@")
        self.assertEqual(expected, "Invalid email")

    def test_that_correct_balance_is_gotten(self):
        actual = pybank.calculate_balance([10000, -100])
        expected = 9900
        self.assertEqual(actual, expected)  

        actual = pybank.calculate_balance([10000, 100])
        expected = 10100
        self.assertEqual(actual, expected) 

        actual = pybank.calculate_balance([10000, -100, 1000, -2000])
        expected = 8900
        self.assertEqual(actual, expected) 

    def test_that_empty_list_return_0(self):
        actual = pybank.calculate_balance([])
        expected = 0
        self.assertEqual(actual, expected) 

    def test_that_password_is_at_least_8_characters_long(self):
        expected = pybank.is_strong_password("Pamilerin")
        self.assertTrue(expected) 

    def test_that_password_is_less_than_8_characters_long(self):
        expected = pybank.is_strong_password("ilerin")
        self.assertFalse(expected) 

    def test_that_correct_final_balance_is_returned(self):
        expected = pybank.apply_interest(5000,0.05,2)
        self.assertEqual(expected,5512.5)
    
    def test_for_rate_is_negative(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000,-0.05,2)

    def test_for_year_is_less_than_one(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000,0.05,0.2)

    def test_transaction_returns_correct_summary(self):
        expected = pybank.get_transaction_summary([["credit", 2000], ["debit", 500], ["credit", 300]])
        actual = [["total_credits", 2300], ["total_debits", 500],["net_balance", 1800], ["transaction_count", 3]]
        self.assertEqual(expected,actual)
                                             
