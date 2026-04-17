"""
collect the user password and it in password variable
password length = len(password)
if password_length is less than eight
print "very weak"
elif password_length is  eight
print "weak"
elif password_length is greater than eight and less than or equal to 16
print "strong"
elif password_length is greater than 16
print "very strong"
"""

password = input("Enter password: ")
password_length = len(password)
if password_length < 8:
    print("very weak")
elif password_length == 8:
    print("weak")
elif password_length > 8 and password_length <= 16:
    print("strong")
elif password_length > 16:
    print("very strong")
