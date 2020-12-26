import pytest
from money.money import Dollar, Franc

@pytest.mark.parametrize(
    "currency, amount, multiplier, expected",
    [
        (Dollar, 5, 2, 10),
        (Dollar, 5, 3, 15),
        (Franc, 5, 2, 10),
        (Franc, 5, 3, 15),
    ]
)
def test_multiplication(currency, amount, multiplier, expected):
    money = currency(amount)
    assert currency(expected) == money.times(multiplier)

@pytest.mark.parametrize(
    "currency",
    [
        Dollar,
        Franc
    ]
)
def test_equality(currency):
    assert currency(5) == currency(5)
    assert currency(5) != currency(4)