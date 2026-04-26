temperature = float(input("Enter a temperature in degree celcius: "))

if temperature < 0:
    print("Freezing\n")

elif temperature >= 0 and temperature <= 15:
    print("Cold\n")

elif temperature >= 16 and temperature <= 25:
    print("Warm\n")

elif temperature > 25:
    print("Hot\n")


    

