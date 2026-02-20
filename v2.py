from decimal import Decimal

def calculate_price(amount, rate):
    return str(Decimal(str(amount)) * Decimal(str(rate)))
