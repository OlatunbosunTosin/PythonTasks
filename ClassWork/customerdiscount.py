"""
Collect the total spending
if the total spending is greater or equal to 1000 and less than or equal 1000.
calculate 5% of the the total spending and subtract it from the total spending
elif the total spending is greater or equal to 10001 and less than or equal 50000.
calculate 10% of the the total spending and subtract it from the total spending
elif the total spending is greater than 50001 
calculate 20% of the the total spending and subtract it from the total spending
else return total spending
"""


total_spending = int(input("Enter total spending: "))
if total_spending >= 1000 and total_spending <= 10000:
        
    discount = (5 /100) * total_spending
    discounted_amount = total_spending - discount
    print("discounted amount = " , discounted_amount)
        

elif total_spending >= 10001 and total_spending <= 50000:
    discount = (10 /100) * total_spending
    discounted_amount = total_spending - discount
    print("discounted amount = " , discounted_amount)
    

elif total_spending > 50001:
    
    discount = (20 /100) * total_spending
    discounted_amount = total_spending - discount
    print("discounted amount = " , discounted_amount)

else: 
    print("total spending = ", total_spending)
    
