import pytest
from app.Calc import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_adding_success(self):
        assert self.calc.adding(self, 2, 2) == 4
    def test_multiply_success(self):
        assert self.calc.multiply(self, 1, 0) == 0
    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 2, 2) == 0
    def test_division_success(self):
        assert self.calc.division(self, 2, 2) == 0
    def teardown(self):
        print('Выполнение метода Teardown')