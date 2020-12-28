import pytest
from money.money import Money, Bank, Expression, Sum

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


def test_currency():
    assert "USD" == Money.dollar(1).currency
    assert "CHF" == Money.franc(1).currency
    assert Money.dollar(5) != Money.franc(5)
    assert Money(1, "CHF") == Money.franc(1)


# def test_addition():
#     sum = Money.dollar(5).sum(Money.dollar(5))
#     assert sum == Money.dollar(10)

#     sum = Money.franc(5).sum(Money.franc(5))
#     assert sum == Money.franc(10)

def test_addition_bank():
    five = Money.dollar(5)
    sum = five.sum(five) # 10 dollars rn
    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reduced

    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(7) == reduced

def test_reduce_single_money():
    bank = Bank()
    reduced = bank.reduce(Money.dollar(2), "USD")
    assert Money.dollar(2) == reduced