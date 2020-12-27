from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return (
            self.amount == other.amount
            and isinstance(self, type(other))
        )

    @abstractmethod
    def times(self, multiplier):
        pass

    def dollar(amount):
        return Dollar(amount, "USD")

    def franc(amount):
        return Franc(amount, "CHF")


class Dollar(Money):
    def times(self, multiplier: int):
        return Money.dollar(self.amount * multiplier)

    # def currency(self):
    #     return "USD"

class Franc(Money):

    def times(self, multiplier: int):
        return Money.franc(self.amount * multiplier)  

    # def currency(self):
    #     return "CHF"