import pytest
from app.calculator import Calculator


class TestCalc():
    def setup(self):
        self.calc = Calculator

    def testing_multiply(self):
        assert self.calc.multiply(self,5, 4) == 20, "Multiply error!"

    def testing_division(self):
        assert self.calc.division(self,20 , 5) == 4, "Divison error!"

    def testing_subtraction(self):
        assert self.calc.subtraction(self, 6, 1) == 5, "Subtraction error!"

    def testing_adding(self):
        assert self.calc.adding(self, 9, 10) == 19, "Adding error!"
