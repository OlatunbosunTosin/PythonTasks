import unittest
import secondssincemidnight

class TestNumberOfSecondsSinceMidnight(unittest.TestCase):

    def test_that_correct_seconds_since_midnight_is_returned(self):
        expected_seconds = secondssincemidnight.seconds_since_midnight(13,30,45)
        actual_seconds = 48645
        self.assertEqual(expected_seconds, actual_seconds)

        expected_seconds = secondssincemidnight.seconds_since_midnight(5,7,10)
        actual_seconds = 18430
        self.assertEqual(expected_seconds, actual_seconds)




