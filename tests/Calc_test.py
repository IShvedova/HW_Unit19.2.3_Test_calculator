import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 0,20) == 0

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 12, 3) == 4

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 343, 300) == 43

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 133, -33) == 100


