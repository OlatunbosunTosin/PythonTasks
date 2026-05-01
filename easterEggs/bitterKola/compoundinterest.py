bank_balance = float(input("Enter bank balance: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
       
first_year_compound_interest = bank_balance * ((1 + (annual_interest_rate / 100)) ** 1)
new_balance_one = bank_balance + first_year_compound_interest

second_year_compound_interest = new_balance_one * ((1 + (annual_interest_rate / 100)) ** 1)
new_balance_two = new_balance_one + second_year_compound_interest;

third_year_compound_interest = new_balance_two * ((1 + (annual_interest_rate / 100)) ** 1)
new_balance_three = new_balance_two + third_year_compound_interest;   
    
print(f"Balance after 1 year is {new_balance_one}, after 2 year is {new_balance_two} and after 3 year is {new_balance_one}")
  
