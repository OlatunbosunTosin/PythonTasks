"""
Initialise passes to 0
for each count in range 1 to 11
    collect either 1 or 2
    while the result is not equal to 1 and 2
        collect either 1 or 2

    if result equals 1
        add 1 to passes
print passes
print counts
calculate failure by subtracting passes from count
print failure


"""

passes = 0

for count in range(1, 11):   
    result = int(input("Enter 1 for pass and 2 for fail: "))  
    while(result != 1 and result != 2):     
        result = int(input("Enter 1 for pass and 2 for fail: "))

    if result == 1:
       passes += 1
print("passes =", passes)
print("count =", count)
failures = count - passes
print("failure =", failure)
       
        



    

