import pytest

from ex_pipeline import add, divide


def test_add_integers() -> None:
    assert add(1, 2) == 3


def test_add_floats() -> None:
    assert add(1.5, 2.5) == 4.0


def test_add_negative() -> None:
    assert add(-1, 1) == 0


def test_add_zero() -> None:
    assert add(0, 0) == 0


def test_divide_basic() -> None:
    assert divide(10, 2) == 5.0


def test_divide_float() -> None:
    assert divide(7, 2) == 3.5


def test_divide_negative() -> None:
    assert divide(-6, 3) == -2.0


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match=r"Cannot divide by zero \(b=0\)"):
        divide(1, 0)


def test_divide_type_error() -> None:
    with pytest.raises(TypeError, match="divide\\(\\) requires numeric arguments"):
        divide("a", 1)  # type: ignore[arg-type]
