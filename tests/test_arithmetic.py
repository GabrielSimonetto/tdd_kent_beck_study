import pytest
from money.money import Money

@pytest.mark.parametrize(
    "currency, amount, multiplier, expected",
    [
        (Money.dollar, 5, 2, 10),
        (Money.dollar, 5, 3, 15),
        (Money.franc, 5, 2, 10),
        (Money.franc, 5, 3, 15),
    ]
)
def test_multiplication(currency, amount, multiplier, expected):
    money = currency(amount)
    assert currency(expected) == money.times(multiplier)


@pytest.mark.parametrize(
    "currency",
    [
        Money.dollar,
        Money.franc
    ]
)
def test_equality(currency):
    assert currency(5) == currency(5)
    assert currency(5) != currency(4)


def test_non_equal_currency():
    assert Money.dollar(5) != Money.franc(5)