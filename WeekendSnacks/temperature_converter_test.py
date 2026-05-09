import unittest
import temperature_converter

class TestForAccuracyOfTemperatureConversion(unittest.TestCase):

    def test_that_celcius_is_accurately_converted_to_fahrenheit(self):
        expected_temperature = temperature_converter.converter("29C")
        actual_temperature = 84.2
        self.assertEqual(expected_temperature,actual_temperature)

    def test_that_fahrenheit_is_accurately_converted_to_celcius(self):
        expected_temperature = temperature_converter.converter("50f")
        actual_temperature = 10
        self.assertEqual(expected_temperature,actual_temperature)

    def test_that_no_unit_is_accurately_converted_to_fahrenheit(self):
        expected_temperature = temperature_converter.converter("29")
        actual_temperature = 84.2
        self.assertEqual(expected_temperature,actual_temperature)

    def test_that_advisary_message_is_accurate(self):
        expected_message = temperature_converter.advisary_message("29", 200)
        actual_message = "Cold advisory"
        self.assertEqual(expected_message,actual_message)

        expected_message = temperature_converter.advisary_message("100f", 10)
        actual_message = "Heat alert"
        self.assertEqual(expected_message,actual_message)


