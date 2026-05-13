import unittest
import averageofarbitaryargument

class TestForAverageOfAnArgumentAndArbitraryArgument(unittest.TestCase):
    
    def test_correct_average_is_returned(self):
        expected_average = averageofarbitaryargument.average(5,10,20,35)
        actual_average = 17.5
        self.assertEqual(expected_average, actual_average)
        
        
