
import pytest
from unittest import TestCase
from context import src
from src.playground import fibbonacci, findCommonNumber
 

class PlayGroundTest(TestCase):

    def test_should_return_one_passing_one(self):
        self.assertEqual(fibbonacci(1),1)

    def test_should_return_one_passing_two(self):
        self.assertEqual(fibbonacci(2),1)
    
    def test_should_return_two_passing_three(self):
        self.assertEqual(fibbonacci(3),2)
    
    def test_should_return_three_passing_four(self):
        self.assertEqual(fibbonacci(4),3)
    
    def test_should_return_five_passing_five(self):
        self.assertEqual(fibbonacci(5),5)
    
    def test_should_return_thirteen_passing_seven(self):
        self.assertEqual(fibbonacci(7),13)

class FindCommonNumber(TestCase):
    def test_should_return_a_list(self):
        self.assertEqual(findCommonNumber([],[]), [])

    def test_should_return_a_list_with_one_element_of_1(self):
        self.assertEqual(findCommonNumber([1],[1]), [1])

    def test_should_return_a_list_with_2_common_elements(self):
        self.assertEqual(findCommonNumber([1,2],[1,2,3]), [1,2])

    def test_should_return_a_list_with_common_elements(self):
        self.assertEqual(findCommonNumber(
            [1,2, 'a'],
            [1,2, 'a', 3]), 
            [1,2, 'a'])
