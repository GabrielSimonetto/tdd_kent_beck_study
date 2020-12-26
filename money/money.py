class Money:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int):
        return Money(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount


class Dollar(Money):
    pass

class Franc(Money):
    pass