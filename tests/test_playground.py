
import pytest
from unittest import TestCase
from context import src
from src.playground import fibbonacci
 

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
