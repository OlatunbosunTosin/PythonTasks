from pybank import *

message = """ 1. Register
2. Login
3. Calculate Balance
4. Apply Interest
5. Summary
6. Exit : """

while True:
    user_input = input("Choose an option: ")
    match user_input:
        case "1":
            email = input("Enter a valid email address: ")
            password = input("Enter a strong password: ")
            if validate_email(email) and is_strong_password(password):
                print("Registration successful")
            else:
                print("Registration unsuccessful")

        case "2":
            email = input("Enter a valid email address: ")
            password = input("Enter a strong password: ")
            if validate_email(email) and is_strong_password(password):
                print("Login successful")
            else:
                print("Login unsuccessful")        
 
        case "3":
            transactions = []
            amount = float(input("Enter transactions or 0 to stop: "))
            while amount != 0:
                transactions.append(amount)
                amount = float(input("Enter transactions or 0 to stop: "))
            total_balance = calculate_balance(transactions)
            print("total balance is", total_balance)

        case "4":
            balance = float(input("Enter balance: "))
            rate = float(input("Enter rate: "))
            years = int(input("Enter number of years: "))
            interest = apply_interest(balance, rate, years)
            print("Your interest you array", interest)
            
        case "5":
            transactions = [] 
            transaction = input("Enter transactions or 0 to stop: ")
            while transaction != 0:
                transactions.append(transaction)
                transaction = input("Enter transactions or 0 to stop: ")

            transaction_summary = get_transaction_summary(transactions)
            print("transaction summary is", transaction_summary) 

    
        case "6":
            break                     
