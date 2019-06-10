num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swapping\nFirst Number: ",num1,"\nSecond Number: ",num2)

# swapping these two numbers without using temp variable

# (num1,num2) = (num2,num1)

# swapping these two numbers without using temp variable. Hence using arithmetic operators
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Swapped without using temp variable")
print("After Swapping\nFirst Number: ",num1,"\nSecond Number: ",num2)