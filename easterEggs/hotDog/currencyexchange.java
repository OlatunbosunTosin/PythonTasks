exchangeRate = float(input("Enter Exchange rate: "))
converter = int(input("Enter 0 to convert from dollars to RMB or 1 to convert from RMB to dollars: "))
amount = float(input("Enter amount: "))

if converter == 0:
    print(f"{amount}USD is {amount * exchangeRate}RMB")

elif converter == 1:
    print(f"{amount}RMB is {amount / exchangeRate}USD")

else:
    print(f"Error, choose between 0 and 1")


