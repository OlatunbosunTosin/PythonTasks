initial_price = float(input("Enter Initial price: "))
discount_percentage = float(input("Enter discount percentage: "))

discount_amount = (discount_percentage / 100) * initial_price
final_price = initial_price - discount_amount;

print(f"Your final price after {discount_percentage} percent discount is {final_price}")
