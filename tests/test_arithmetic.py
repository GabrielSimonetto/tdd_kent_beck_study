import pytest
from money.dollar import Dollar

@pytest.mark.parametrize(
    "amount, multiplier, expected",
    [
        (5, 2, 10),
        (5, 3, 15),
    ]
)
def test_multiplication_pytest_version(amount, multiplier, expected):
    dollar = Dollar(amount)
    assert Dollar(expected) == dollar.times(multiplier)


def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(4)