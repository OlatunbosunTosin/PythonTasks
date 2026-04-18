for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()

#prints > when row == 0 and < when row == 1, for loop column prints 10 < and > for reach row
