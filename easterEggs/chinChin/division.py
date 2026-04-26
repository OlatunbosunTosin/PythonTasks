numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))        


if denominator == 0:
    print(f"You cannot divide by 0")

else:
    division = numerator / denominator
    print(f"{numerator} / {denominator} = {division}")

