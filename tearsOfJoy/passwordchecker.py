"""
19. Password retry loop
Ask for a password up to 3 times. Print 'Access granted' if correct, 'Locked out' after 3 wrong attempts.
Correct password: python123
Expected output: Password: wrong / Password: wrong / Password: python123 / Access granted
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




