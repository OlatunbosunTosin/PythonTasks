"""
print number\tsquare\tcube
for each number in range (6)
    for each square in range (6)
        calculate squared_number = number * number
        for each cube in range (6):
            calculate cubed_number = number * number * number
    print number,squared_number,cubed_number

"""



print("number\tsquare\tcube")
for number in range (6):
    for square in range (6):
        squared_number = number * number
        for cube in range (6):
            cubed_number = number * number * number
    print(f"{number:>6}\t{squared_number:>6}\t{cubed_number:>4}")
   
    



    
