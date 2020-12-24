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
    product = dollar.times(multiplier)
    assert expected == product.amount


def test_multiplication_book_version():
    amount = 5

    multiplier = 2
    five = Dollar(amount)
    product = five.times(multiplier) 
    expected = amount * multiplier
    assert expected == product.amount

    multiplier = 3
    product = five.times(multiplier) 
    expected = amount * multiplier
    assert expected == product.amount