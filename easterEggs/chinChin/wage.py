hourly_wage = float(input("Enter hourly wage: "))
hours_worked = float(input("Enter hours worked: "))

total_earnings = 0

if hours_worked <= 40:
    total_earnings = hourly_wage * hours_worked
    print(f"Your total earning is {total_earnings}\n")

elif hours_worked > 40:
    total_earnings = (40 * hourly_wage) + ((hours_worked - 40) * hourly_wage * 1.5)
    print(f"Your total earning is {total_earnings}\n")

