weight = float(input("Enter weight of package: "))

if weight > 0 and weight <= 2:
    print("Shipping is $2.5\n")

elif weight > 2 and weight <= 4:
    print("Shipping is $4.5\n")

elif weight > 4 and weight <= 10:
    print("Shipping is $7.5\n")

elif weight > 10 and weight <= 20:
    print("Shipping is $10.5\n")

elif weight > 20:
    print("Shipping is The package cannot be shipped\n")

else:
    print("Try again")

