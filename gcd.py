# taking first number
num1 = int(input("Enter first number: "))               
# taking second number
num2 = int(input("Enter second number: "))              

gcd = 1

# finding GCD
for i in range(min(num1,num2),0,-1):                    
    if (num1%i) == 0 and (num2%i) == 0:
        gcd = i
        break
    
# printing GCD
print("The GCD of the two numbers is ", gcd)             