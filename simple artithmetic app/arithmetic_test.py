import unittest

from arithmetic import *


class TestArithmetic(unittest.TestCase):
    def test_correct_answer(self):
        num1,num2,answer= generate_subtraction_problem()
        self.assertEqual(answer,num1-num2)
    def test_num1_is_bigger(self):
        num1,num2,answer= generate_subtraction_problem()
        self.assertEqual(num1,max(num1,num2))
    def test_num2_is_smaller(self):
        num1,num2,answer= generate_subtraction_problem()
        self.assertEqual(num2,min(num1,num2))
