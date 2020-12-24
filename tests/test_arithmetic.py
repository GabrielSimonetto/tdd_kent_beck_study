from money.dollar import Dollar

def test_multiplication():
    amount = 5

    multiplier = 2
    five = Dollar(amount)
    product = five.times(multiplier) 
    expected = amount * multiplier
    assert expected == product.amount

    multiplier = 3
    product = five.times(multiplier) 
    expected = amount * multiplier
    assert expected == product.amount