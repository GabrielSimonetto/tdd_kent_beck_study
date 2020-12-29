import pytest
from money.money import Money, Bank, Sum

@pytest.fixture
def bank():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    # bank.add_rate("USD", "USD", 1)
    # bank.add_rate("CHF", "CHF", 1)
    return bank


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

def test_addition_bank(bank):
    five = Money.dollar(5)
    sum = five.sum(five) # 10 dollars rn
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reduced

    sum = Sum(Money.dollar(3), Money.dollar(4))
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(7) == reduced

def test_reduce_single_money(bank):
    bank = Bank()   
    reduced = bank.reduce(Money.dollar(2), "USD")
    assert Money.dollar(2) == reduced

def test_reduce_different_currency_money(bank):
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result

def test_identity_rate(bank):
    assert 1 == bank.get_rate("USD", "USD")

def test_mixed_addition(bank):
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    # result = bank.reduce(five_bucks.sum(ten_francs))
    sum = Sum(five_bucks, ten_francs)
    result = bank.reduce(sum, "USD")
    assert result == Money.dollar(10)

def test_sum_plus_money(bank):
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    # result = bank.reduce(five_bucks.sum(ten_francs))
    sum = Sum(five_bucks, ten_francs).sum(five_bucks)
    result = bank.reduce(sum, "USD")
    assert result == Money.dollar(15)

def test_sum_plus_money(bank):
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    sum = Sum(five_bucks, ten_francs).times(2)
    result = bank.reduce(sum, "USD")
    assert result == Money.dollar(20)
