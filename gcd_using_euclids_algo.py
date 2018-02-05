num1 = int(input("Enter first number: "))           # taking first number
num2 = int(input("Enter second number: "))          # taking second number

if num2 > num1:                                     # checking if num2 is greater than num1 then swap these numbers
    (num1,num2) = (num2,num1)

while num1%num2 != 0:                               # repeat these steps till num2 divides num1 with remainder zero
    (num1,num2) = (num2,num1%num2)                  # swap num1 to num2 and num2 with remainder

print("The GCD of the numbers is ",num2)            # printing GCD