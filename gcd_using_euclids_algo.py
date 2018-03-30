# taking first number
num1 = int(input("Enter first number: "))
# taking second number           
num2 = int(input("Enter second number: "))          

# checking if num2 is greater than num1 then swap these numbers
if num2 > num1:                                     
    (num1,num2) = (num2,num1)
# repeat these steps till num2 divides num1 with remainder zero
while num1%num2 != 0:                              
    # swap num1 to num2 and num2 with remainder
    (num1,num2) = (num2,num1%num2)                  

# printing GCD
print("The GCD of the numbers is ",num2)            