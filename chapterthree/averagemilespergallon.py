"""
intialise average to 0
initialise count to 0
initialise sum to 0
collect miles_driven from user
colect gallons used
while miles driven is not equal to -1
    add one to count
    calculate miles_per_gallon
    print miles_per_gallon for each tank
    calculate sum 
    collect miles_driven from user
    colect gallons used
    calculate average
print average
    

"""

combined_miles_per_gallon = 0
count = 0
average = 0

miles_driven = float(input("Enter miles driven (-1 to end): "))
gallons_used = float(input("Enter gallons used: "))
while miles_driven != -1:
    count = count + 1
    miles_per_gallon = miles_driven / gallons_used
    print(f"miles per gallon for this tank is {miles_per_gallon:.6f}")
    combined_miles_per_gallon += miles_per_gallon
    miles_driven = float(input("Enter miles driven (-1 to end): "))
    gallons_used = float(input("Enter gallons used: "))
    average = combined_miles_per_gallon / count
print(f"overall average miles per gallon is {average:.6f}")
    
