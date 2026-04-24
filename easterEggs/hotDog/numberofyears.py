minutes = int(input("Enter number of minutes: "))
years = ((minutes // 60) // 24) // 365
days = ((minutes // 60) // 24) % 365;
print(f"{minutes} minutes is {years} years and {days} days")
    
