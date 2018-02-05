num = int(input("Enter a number: "))        # taking input from user

fac = 1                                     # initializing the initial value of fac
for i in range(1,num+1):                    # running for loop 
    fac = fac * i                           # multiplying previous fac value to i and store it back in fac variable
print("The factorial of number is ",fac)    # printing the factorial of number