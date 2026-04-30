# Test for the calculator functions
from calculadora import Calculator

import pytest
from calculadora import Calculator

@pytest.fixture
def calculator():
    return Calculator(10, 5)

def test_given_two_numbers_when_add_then_sum_is_returned(calculator):
    assert calculator.add() == 15

def test_given_two_numbers_when_subtract_then_difference_is_returned(calculator):
    assert calculator.subtract() == 5

def test_given_two_numbers_when_multiply_then_product_is_returned(calculator):
    assert calculator.multiply() == 50

def test_given_two_numbers_when_divide_then_quotient_is_returned(calculator):
    assert calculator.divide() == 2

def test_given_division_by_zero_when_divide_then_error_is_returned():
    calculator_zero = Calculator(10, 0)
    assert calculator_zero.divide() == "Error: Division by zero"

def test_given_negative_numbers_when_add_then_sum_is_returned():
    calculator = Calculator(-3, -7)
    assert calculator.add() == -10

def test_given_negative_and_positive_when_add_then_sum_is_returned():
    calculator = Calculator(-3, 7)
    assert calculator.add() == 4

def test_given_zero_when_add_then_sum_is_returned():
    calculator = Calculator(0, 5)
    assert calculator.add() == 5

def test_given_floats_when_add_then_sum_is_returned():
    calculator = Calculator(2.5, 3.1)
    assert pytest.approx(calculator.add(), 0.01) == 5.6

def test_given_large_numbers_when_add_then_sum_is_returned():
    calculator = Calculator(1_000_000, 2_000_000)
    assert calculator.add() == 3_000_000

def test_given_same_numbers_when_subtract_then_zero_is_returned():
    calculator = Calculator(5, 5)
    assert calculator.subtract() == 0

def test_given_negative_numbers_when_subtract_then_difference_is_returned():
    calculator = Calculator(-5, -2)
    assert calculator.subtract() == -3

def test_given_zero_when_subtract_then_difference_is_returned():
    calculator = Calculator(0, 5)
    assert calculator.subtract() == -5

def test_given_floats_when_subtract_then_difference_is_returned():
    calculator = Calculator(5.5, 2.2)
    assert pytest.approx(calculator.subtract(), 0.01) == 3.3

def test_given_large_numbers_when_subtract_then_difference_is_returned():
    calculator = Calculator(2_000_000, 1_000_000)
    assert calculator.subtract() == 1_000_000

def test_given_zero_when_multiply_then_zero_is_returned():
    calculator = Calculator(0, 5)
    assert calculator.multiply() == 0

def test_given_negative_numbers_when_multiply_then_product_is_returned():
    calculator = Calculator(-3, -2)
    assert calculator.multiply() == 6

def test_given_negative_and_positive_when_multiply_then_product_is_returned():
    calculator = Calculator(-3, 2)
    assert calculator.multiply() == -6

def test_given_floats_when_multiply_then_product_is_returned():
    calculator = Calculator(2.5, 4.0)
    assert pytest.approx(calculator.multiply(), 0.01) == 10.0

def test_given_large_numbers_when_multiply_then_product_is_returned():
    calculator = Calculator(1_000, 2_000)
    assert calculator.multiply() == 2_000_000

def test_given_zero_when_divide_then_zero_is_returned():
    calculator = Calculator(0, 5)
    assert calculator.divide() == 0

def test_given_negative_numbers_when_divide_then_quotient_is_returned():
    calculator = Calculator(-10, -2)
    assert calculator.divide() == 5

def test_given_negative_and_positive_when_divide_then_quotient_is_returned():
    calculator = Calculator(-10, 2)
    assert calculator.divide() == -5

def test_given_floats_when_divide_then_quotient_is_returned():
    calculator = Calculator(5.5, 2.2)
    assert pytest.approx(calculator.divide(), 0.01) == 2.5

def test_given_large_numbers_when_divide_then_quotient_is_returned():
    calculator = Calculator(2_000_000, 1_000)
    assert calculator.divide() == 2000

def test_given_zero_dividend_and_zero_divisor_when_divide_then_error_is_returned():
    calculator = Calculator(0, 0)
    assert calculator.divide() == "Error: Division by zero"

    

