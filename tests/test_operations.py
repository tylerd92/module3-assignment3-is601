""" tests/test_operations.py """
import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition_positive():
    """Test positive cases for addition."""
    assert addition(4, 6) == 10
    assert addition(0, 3) == 3
    assert addition(-5, 5) == 0

def test_addition_negative():
    """Test negative cases for addition."""
    assert addition(-3, -1) == -4
    assert addition(0, -2) == -2
    
def test_subtraction_positive():
    """Test positive cases for subtraction."""
    assert subtraction(8, 3) == 5
    assert subtraction(10, -6) == 16

def test_subtraction_negative():
    """Test negative cases for subtraction."""
    assert subtraction(-5, -3) == -2
    assert subtraction(4, 7) == -3

def test_multiplication_positive():
    """Test positive cases for multiplication."""
    assert multiplication(5, 7) == 35
    assert multiplication(8, 1) == 8
    assert multiplication(-4, -6) == 24

def test_multiplication_negative():
    """Test negative cases for multiplication."""
    assert multiplication(4, -5) == -20
    assert multiplication(-3, 3) == -9

def test_division_positive():
    """Test positive cases for division."""
    assert division(12, 2) == 6
    assert division(-10, -2) == 5

def test_divistion_negative():
    """Test negative cases for division."""
    assert division(-12, 2) == -6
    assert division(14, -7) == -2

def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(5, 0)