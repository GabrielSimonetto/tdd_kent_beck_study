from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return (
            self.amount == other.amount
            and self.currency == other.currency
        )

    def times(self, multiplier, currency):
        return Money(self.amount * multiplier, currency)

    def dollar(amount, currency="USD"):
        return Dollar(amount, currency)

    def franc(amount, currency="CHF"):
        return Franc(amount, currency)


class Dollar(Money):
    def times(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency)

    # def currency(self):
    #     return "USD"

class Franc(Money):
    def times(self, multiplier: int):
        return Money.franc(self.amount * multiplier, self.currency)  

    # def currency(self):
    #     return "CHF"