"""
for each row from 1 to 6
    for rach column from row
        print colum
    print()
"""

for row in range(1,6):
    for column in range(1,row+1):
        print(column, end=" ")
    print()


