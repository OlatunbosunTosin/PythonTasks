seconds = int(input("Enter number of seconds: "))
hours = (seconds // 60) // 60
minutes = ((seconds // 60) % 60) % 60
remaining_seconds = seconds % 60
    
print(f"{seconds} seconds = {hours} hours, {minutes} minutes, {remaining_seconds} seconds")

