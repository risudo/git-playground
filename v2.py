def calculate_price(amount, rate):
    # バグ: rateが0の時にエラーが起きる可能性
    return amount * rate
