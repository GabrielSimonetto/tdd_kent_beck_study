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

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def dollar(amount):
        return Money(amount, "USD")

    def franc(amount):
        return Money(amount, "CHF")
