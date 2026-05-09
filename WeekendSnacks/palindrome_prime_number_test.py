import unittest
import palindrome_prime_number

class TestForCorrectDiscountPrice(unittest.TestCase):

    def test_that_number_is_both_palindrome_and_prime_number(self):
        
        self.assertTrue(palindrome_prime_number.palindrome_prime_number_checker(131))

    def test_that_number_is_not_both_palindrome_and_prime_number(self):
        self.assertFalse(palindrome_prime_number.palindrome_prime_number_checker(121))

   

