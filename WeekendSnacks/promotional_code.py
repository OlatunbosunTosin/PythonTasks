def discount_price(name_of_item, original_price, promotional_code):
    new_price = 0.0
    if promotional_code == "SAVE10":
        discount = (10/100) * original_price
        new_price = original_price - discount
    elif promotional_code == "HALFOFF":
        discount = (50/100) * original_price
        new_price = original_price - discount
    else:
        new_price = original_price

    return new_price
