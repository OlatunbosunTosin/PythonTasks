salary = float(input("Enter monthly salary: "))

tax_owed = 0;

if salary <= 300000:
    print("No tax owed")

elif salary > 300000 and salary <= 600000:
    tax_owed = 0.15 * salary
    print(f"Tax owed is {tax_owed}")

elif salary > 600000:
    tax_owed = 0.25 * salary
    print(f"Tax owed is {tax_owed}")
