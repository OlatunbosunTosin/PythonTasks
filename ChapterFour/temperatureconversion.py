def fahrenheit_to_celcius():
    return (1.8) * number + 32


print(f"Celcius\t\tfahrenheit")
for number in range(101):
    print(f"{number:<3}{fahrenheit_to_celcius():18.2f}")
