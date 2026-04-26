first_edge = float(input("Enter first edge: "))
second_edge = float(input("Enter second edge: "))

perimeter = 2 * (first_edge + second_edge)

if first_edge != second_edge:
    print(f"Perimiter = {perimeter}")

else:
    print("Input is invalid")


