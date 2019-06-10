# taking input from user
num = int(input("Enter a number: "))        

# initializing the initial value of fac
fac = 1                                     
# running for loop 
for i in range(1,num+1):                    
    # multiplying previous fac value to i and store it back in fac variable
    fac = fac * i                 
          
# printing the factorial of number
print("The factorial of number is ",fac)    