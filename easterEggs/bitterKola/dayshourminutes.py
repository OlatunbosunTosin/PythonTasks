minutes = int(input("Enter time minutes: "))
days = (minutes // 60) // 24
hours = ((minutes // 60) % 24)
remaining_minutes = minutes % 60

print(f"{minutes} minutes is {days} day(s), {hours} hours and {remaining_minutes} minutes")
 
