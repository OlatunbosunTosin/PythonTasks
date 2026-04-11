seconds = int(input("Enter seconds: "))
hours = seconds // 60 // 60
minutes = seconds // 60 % 60
remaining_seconds = seconds % 60
print(hours, "hour,", minutes, "minute,", remaining_seconds, "second") 
