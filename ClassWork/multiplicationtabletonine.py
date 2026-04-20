print(f"{"Multiplicaton Table":^38}")

for count in range(1, 10):
    print(count, end=" |")
    
    for number in range(1, 10):
        multiply = number * count
        print(f"{multiply:>3}",end=" ")
    print()
