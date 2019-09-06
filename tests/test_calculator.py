from unittest import TestCase
from context import src
from src.hotel import Hotel
from src.calculator import Calculator

customerType, period = 'regular',['SUN','MON','TUE']
class CalculatorTest(TestCase):
    
    def test_should_return_name_of_the_cheapper_hotel(self):
        calculator = Calculator()
        self.assertEqual(calculator.getCheappest(customerType, period), '')
    
    def test_should_return_name_of_the_cheapper_hotel_when_pass_one_hotel(self):
        hotels = [Hotel('LakeWood', 8, 10, 20, 25, 1)]
        calculator = Calculator(hotels)
        self.assertEqual(calculator.getCheappest(customerType, period), 'LakeWood')

    def test_should_return_name_of_the_cheapper_hotel_when_pass_two_hotels(self):
        hotels = [Hotel('LakeWood', 8, 10, 20, 25, 1), Hotel('Wood', 10, 20, 20, 25, 1)]
        calculator = Calculator(hotels)
        self.assertEqual(calculator.getCheappest(customerType, period), 'LakeWood')

    def test_should_return_name_of_the_second_hotel_because_its_cheaper(self):
        hotels = [Hotel('Wood', 10, 20, 20, 25, 1), Hotel('LakeWood', 8, 10, 20, 25, 1)]
        calculator = Calculator(hotels)
        self.assertEqual(calculator.getCheappest(customerType, period), 'LakeWood')

    def test_should_return_name_of_the_cheapper_hotel_when_pass_two_hotels_with_same_price(self):
        hotels = [Hotel('LakeWood', 10, 20, 20, 25, 1), Hotel('Wood', 10, 20, 20, 25, 2)]
        calculator = Calculator(hotels)
        self.assertEqual(calculator.getCheappest(customerType, period), 'Wood')
