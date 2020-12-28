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

    def reduce(self, currency_to):
        return self


class Bank:
    def reduce(self, expression_source, currency_to):
        return expression_source.reduce(currency_to)

        # if isinstance(expression_source, Money):
        #     return Money(expression_source.amount, currency_to)

        # return Money(
        #     expression_source.augend.amount + expression_source.addend.amount,
        #     currency_to)

class Expression(ABC):
    pass

class Sum(Expression):
    def __init__(self, augend: Money, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, currency_to):
        return Money(
            self.augend.amount + self.addend.amount,
            currency_to
        )        
