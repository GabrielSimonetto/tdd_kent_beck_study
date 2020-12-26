from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount: int):
        self.amount = amount

    def __eq__(self, other):
        return (
            self.amount == other.amount
            and isinstance(self, type(other))
        )

    @abstractmethod
    def times(self, multiplier):
        pass

    def dollar(amount):
        return Dollar(amount)

    def franc(amount):
        return Franc(amount)


class Dollar(Money):
    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

class Franc(Money):
    def times(self, multiplier: int):
        return Franc(self.amount * multiplier)  