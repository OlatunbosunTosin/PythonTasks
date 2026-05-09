import unittest
import promotional_code

class TestForCorrectDiscountPrice(unittest.TestCase):

    def test_for_correct_ten_percent_discount_(self):
        expected_discount_price = promotional_code.discount_price("soap", 3000, "SAVE10",)
        actual_discount_price = 2700
        self.assertEqual(expected_discount_price,actual_discount_price)

    def test_for_correct_fifty_percent_discount_(self):
        expected_discount_price = promotional_code.discount_price("soap", 3000, "HALFOFF",)
        actual_discount_price = 1500
        self.assertEqual(expected_discount_price,actual_discount_price)

    def test_for_invalidcode_discount_(self):
        expected_discount_price = promotional_code.discount_price("soap", 3000, "SAV",)
        actual_discount_price = 3000
        self.assertEqual(expected_discount_price,actual_discount_price)

   

