import pytest
from money.money import Money, Bank, Sum

@pytest.fixture
def bank():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    bank.add_rate("USD", "CHF", 0.5)
    return bank

@pytest.fixture
def four_bucks():
    return Money.dollar(4)

@pytest.fixture
def four_francs():
    return Money.franc(4)


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
    assert currency(expected) == money * multiplier


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


def test_currency(four_bucks, four_francs):
    assert "USD" == four_bucks.currency
    assert "CHF" == four_francs.currency
    assert four_bucks != four_francs
    assert Money(4, "CHF") == four_francs


def test_addition(four_bucks):
    sum = four_bucks + four_bucks
    expected = 8
    assert sum == Money.dollar(expected)


def test_addition_bank(bank, four_bucks):
    sum = four_bucks + four_bucks
    reduced = bank.reduce(sum, "USD")
    expected = 8
    assert Money.dollar(expected) == reduced

    sum = Money.dollar(3) + Money.dollar(0)
    reduced = bank.reduce(sum, "USD")
    expected = 3
    assert Money.dollar(expected) == reduced

def test_reduce_single_money(bank, four_bucks):
    bank = Bank()   
    reduced = bank.reduce(four_bucks, "USD")
    assert four_bucks == reduced

def test_reduce_different_currency_money(bank, four_francs):
    result = bank.reduce(four_francs, "USD")
    expected = 2
    assert Money.dollar(expected) == result

def test_identity_rate(bank):
    assert 1 == bank.get_rate("USD", "USD")

def test_mixed_addition(bank, four_bucks, four_francs):
    sum = Sum(four_bucks, four_francs)
    result = bank.reduce(sum, "USD")
    expected = 6
    assert result == Money.dollar(expected)

def test_sum_plus_money(bank, four_bucks, four_francs):
    sum = four_bucks + four_francs + four_bucks
    result = bank.reduce(sum, "USD")
    expected = 10
    assert result == Money.dollar(expected)

    result = bank.reduce(sum, "CHF")
    expected = 20
    assert result == Money.franc(expected)

def test_sum_plus_money(bank, four_bucks, four_francs):
    sum = (four_bucks + four_francs) * 2
    result = bank.reduce(sum, "USD")
    expected = 12
    assert result == Money.dollar(expected)


    