def add(a: int | float, b: int | float) -> int | float:
    return a + b


def divide(a: int | float, b: int | float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        ta, tb = type(a).__name__, type(b).__name__
        raise TypeError(f"divide() requires numeric arguments, got {ta} and {tb}")
    if b == 0:
        raise ValueError(f"Cannot divide by zero (b={b!r})")
    return a / b
