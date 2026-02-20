def calculate_price(amount, rate):
    # バグ修正: rateが0の時のチェックを追加
    if rate == 0:
        return 0
    return amount * rate
