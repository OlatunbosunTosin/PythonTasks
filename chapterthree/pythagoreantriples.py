"""
print heading of the triple sides
for each hypotenuse in range 1 to 21
    calculate hypothenuse_square = hypothenuse * hypothenuse
    for each opposite in range 1 to 21
        calculate pposite_square = opposite * opposite
        for each adjacent in range1 to 21
            calculate adjacent_square = adjacent * adjacent
            calculate sum_of_two_sides = opposite_square + adjacent_square
            if hypothenuse_square == sum_of_two_sides
                print hypotenuse, opposite, adjacent
"""



print(f"hypothenuse\topposite\tadjacent")
for hypothenuse in range(1,21):
    hypothenuse_square = hypothenuse * hypothenuse
    for opposite in range(1,21):
        opposite_square = opposite * opposite
        for adjacent in range(1,21):
            adjacent_square = adjacent * adjacent
            sum_of_two_sides = opposite_square + adjacent_square
            if hypothenuse_square == sum_of_two_sides:
    
                print(f"{hypothenuse:>11}\t{opposite:>8}\t{adjacent:>8}")

    



