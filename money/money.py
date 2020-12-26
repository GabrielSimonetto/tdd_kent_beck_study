class Money:
    def __init__(self, amount: int):
        self.amount = amount

    def __eq__(self, other):
        return (
            self.amount == other.amount
            and isinstance(self, type(other))
        )


class Dollar(Money):
    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

class Franc(Money):
    def times(self, multiplier: int):
        return Franc(self.amount * multiplier)