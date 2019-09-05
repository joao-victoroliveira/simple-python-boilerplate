from unittest import TestCase
from context import src
from src.calculator import Calculator

class CalculatorTest(TestCase):
    
    def test_should_return_name_of_the_cheapper_hotel(self):
        calculator = Calculator()
        self.assertEqual(calculator.getCheappest(), '')
