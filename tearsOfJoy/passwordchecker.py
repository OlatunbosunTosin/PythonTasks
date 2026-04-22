"""
set number to 0
set count to 0
Initialise password to empty string
while number is less than 3
    collect password
    if password equals python123
        print Access granted
        break
    Increment count by 1
    if count equals 3
        print Locked out
    
"""



number = 0
count = 0
password = " "
while number < 3:

    password = input("Enter password: ")
    if password == "python123":
        print("Access granted")
        break

    count += 1
    if count == 3:
        print("Locked out")




