"""Basic arithmetic operations"""

Number = int | float


def add(a: Number, b: Number) -> Number:
    """Return a + b."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return a - b."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return a * b."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return a / b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("tinycalc: cannot divide by zero")
    return a / b
