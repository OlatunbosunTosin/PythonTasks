import unittest
import arbitraryargumentlist

class TestForProductOfAnArbitraryArgumentList(unittest.TestCase):
    
    def test_correct_product_is_returned_for_two_arguments(self):
        expected_product = arbitraryargumentlist.product_of_arbitary_argument_list(1,10)
        actual_product = 10
        self.assertEqual(expected_product, actual_product)
        
    def test_correct_product_is_returned_for_three_arguments(self):
        expected_product = arbitraryargumentlist.product_of_arbitary_argument_list(1,10,5)
        actual_product = 50
        self.assertEqual(expected_product, actual_product)
        
    def test_correct_product_is_returned_for_four_arguments(self):
        expected_product = arbitraryargumentlist.product_of_arbitary_argument_list(1,5,4,5)
        actual_product = 100
        self.assertEqual(expected_product, actual_product)    
        
        
