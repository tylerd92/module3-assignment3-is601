""" tests/test_operations.py """
import pytest
from typing import Union
from app.operations import Operations

Number = Union[int, float]

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 6, 10),
        (0, 3, 3),
        (-5, 5, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ],
    ids=[
        "add_two_positive_integers",
        "add_zero_and_positive_integer",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float"
    ]
)

def test_addition(a: Number, b: Number, expected: Number) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"
    
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (8, 3, 5),
        (0, 0, 0),
        (-5, -3, -2),
        (9.5, 5.5, 4.0),
        (-8.5, -4.5, -4.0),
    ],
    ids=[
        "subtract_positive_integer_from_larger",
        "subtract_two_zeros",
        "subtract_negative_integer_from_negative_integer",
        "subtract_two_positive_floats",
        "subtract_two_begative_floats"
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

def test_multiplication_positive():
    """Test positive cases for multiplication."""
    assert Operations.multiplication(5, 7) == 35
    assert Operations.multiplication(8, 1) == 8
    assert Operations.multiplication(-4, -6) == 24

def test_multiplication_negative():
    """Test negative cases for multiplication."""
    assert Operations.multiplication(4, -5) == -20
    assert Operations.multiplication(-3, 3) == -9

def test_division_positive():
    """Test positive cases for division."""
    assert Operations.division(12, 2) == 6
    assert Operations.division(-10, -2) == 5

def test_divistion_negative():
    """Test negative cases for division."""
    assert Operations.division(-12, 2) == -6
    assert Operations.division(14, -7) == -2

def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(5, 0)