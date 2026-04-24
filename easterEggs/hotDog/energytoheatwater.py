quantity = float(input("Enter amount of water: "))
initialTemperature = float(input("Enter Initial temperature: "))
finalTemperature = float(input("Enter final temperature: "))

energy_needed = quantity * (finalTemperature - initialTemperature) * 4184;
print(f"Energy needed to heat {quantity} kg of water is {energy_needed}" )

