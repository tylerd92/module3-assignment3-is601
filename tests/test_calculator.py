""" tests/test_calculator.py """
import sys
from io import StringIO
from app.calculator import calculator

"""
:param monkeypatch: a pytest fixture to simulate user input
:param inputs: list of inputs to simulate
:return: captured output as a string
"""
def run_calculator_with_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

# Positive Tests
def test_addition(monkeypatch):
    """Test addition operation in REPL."""
    inputs = ["add 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_subtraction(monkeypatch):
    """Test subtraction operation in REPL."""
    inputs = ["subtract 10 7", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output

def test_multiplication(monkeypatch):
    """Test multiplication operation in REPL."""
    inputs = ["multiply 8 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 24.0" in output

def test_division(monkeypatch):
    """Test division operation in REPL."""
    inputs = ["divide 12 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 6.0" in output

# Negative Tests
def test_invalid_operation(monkeypatch):
    """Test invalid operatio in REPL."""
    inputs = ["modulus 12 6", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Unknown operation" in output

def test_invalid_input_format(monkeypatch):
    """Test invalid input format in repl"""
    inputs = ["multiply eight three", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input. Please follow the format" in output

def test_division_by_zero(monkeypatch):
    """Test division by zero"""
    inputs = ["divide 4 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed" in output