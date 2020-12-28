from abc import ABC, abstractmethod

class Money:
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return (
            self.amount == other.amount
            and self.currency == other.currency
        )

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    # def sum(self, other):
    #     return Money(self.amount + other.amount, self.currency)

    def sum(self, other):
        return Sum(self, other)

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def dollar(amount):
        return Money(amount, "USD")

    def franc(amount):
        return Money(amount, "CHF")

    def reduce(self, currency_to, bank):
        rate = bank.get_rate(self.currency, currency_to)
        return Money(self.amount // rate, currency_to)


class Bank:
    def __init__(self):
        self.rates = dict()

    def reduce(self, expression_source, currency_to):
        return expression_source.reduce(currency_to, self)

    def add_rate(self, _from, to, rate):
        self.rates[CurrencyPair(_from, to)] = rate

    def get_rate(self, currency_from, currency_to):
        if currency_from == currency_to:
            return 1

        return self.rates[CurrencyPair(currency_from, currency_to)]
        # return 2 if (currency_from == "CHF" and currency_to == "USD") else 1

class CurrencyPair():
    def __init__(self, _from, to):
        self._from = _from
        self.to = to

    def __hash__(self):
        return 0

    def __repr__(self):
        return f"({self._from}: {self.to})"

    def __eq__(self, other):
        return (
            self._from == other._from
            and self.to == other.to
        )

class Expression(ABC):
    pass

class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, currency_to, bank):
        amount = (
            self.augend.reduce(currency_to, bank).amount
            + self.addend.reduce(currency_to, bank).amount
        )

        return Money(amount, currency_to)        
