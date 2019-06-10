# defining gcd function
def gcd(num1,num2):
    if num1%num2 == 0:
        # Base case
        return num2
    else:
        # Iterative case
        return gcd(num2,num1%num2)

# taking first number
num1 = int(input("Enter first number: "))
# taking second number           
num2 = int(input("Enter second number: "))          

# checking if num2 is greater than num1 then swap these numbers
if num2 > num1:                                     
    (num1,num2) = (num2,num1)

# printing GCD
print("The GCD of the numbers is",gcd(num1,num2))  